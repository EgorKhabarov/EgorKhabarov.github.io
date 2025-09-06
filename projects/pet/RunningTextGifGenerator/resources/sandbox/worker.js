// resources/sandbox/worker.js
importScripts("https://cdn.jsdelivr.net/pyodide/v0.28.2/full/pyodide.js");
//import { loadPyodide } from "https://cdn.jsdelivr.net/pyodide/v0.28.2/full/pyodide.mjs";

function start_text_spinner(text) {
    self.postMessage({type: "stop_spinner"});
    self.postMessage({type: "log", text: text});
    self.postMessage({type: "start_spinner"});
}
function stop_text_spinner() {
    self.postMessage({type: "stop_spinner"});
    self.postMessage({type: "log", text: " Done\n"});
}


// worker.js
const pyodideReadyPromise = (async () => {
    self.postMessage({type: "log_clean"});
    start_text_spinner("Loading... Please wait ");

    const pyodide = await loadPyodide();

    start_text_spinner("\nLoading libraries... ");
    await pyodide.loadPackage(["micropip", "pillow"]);
    stop_text_spinner();

    start_text_spinner("Loading fonts... ");
    try {pyodide.FS.mkdir("/fonts");} catch(e) {}
    const resp = await fetch("/projects/pet/RunningTextGifGenerator/resources/sandbox/Monocraft.otf");
    const bytes = new Uint8Array(await resp.arrayBuffer());
    pyodide.FS.writeFile("/fonts/Monocraft.otf", bytes);
    stop_text_spinner();

    // function listdir(currentPath = "/") {
    //     const entries = pyodide.FS.readdir(currentPath);
    //     let results = [];
    //     for (const entry of entries) {
    //         if (entry === "." || entry === "..") continue;
    //         const fullPath = currentPath + (currentPath === "/" ? "" : "/") + entry;
    //         results.push(fullPath);
    //     }
    //     console.log(`"${currentPath}"`, results);
    // }
    // listdir();
    // listdir("/fonts");

    self.send_log = (txt) => {self.postMessage({type: "log", text: txt});}
    self.send_err = (txt) => {self.postMessage({type: "err", text: txt});}
    self.postMessage({type: "log", text: "Ready!\n"});
    self.postMessage({type: "log_clean"});
    return pyodide;
})();




self.onmessage = async (event) => {
    const {type, code} = event.data;
    if (type !== "run") return;

    const pyodide = await pyodideReadyPromise;

    try {
        // оборачиваем код для перехвата stdout/stderr
        const wrapped = `
import sys
from js import send_log, send_err

class JsStdout:
    def write(self, s):
        send_log(s)
    def flush(self):
        pass

class JsStderr:
    def write(self, s):
        send_err(s)
    def flush(self):
        pass

sys.stdout = JsStdout()
sys.stderr = JsStderr()

${code}
`;
        let result = await pyodide.runPythonAsync(wrapped);
        self.postMessage({type: "done", result});
    } catch (err) {
        self.postMessage({type: "error", error: err.message});
    }
};

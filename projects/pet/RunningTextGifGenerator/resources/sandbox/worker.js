importScripts("https://cdn.jsdelivr.net/pyodide/v0.28.2/full/pyodide.js");

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

    self.send_log = (txt) => {self.postMessage({type: "log", text: txt});}
    self.send_err = (txt) => {self.postMessage({type: "err", text: txt});}
    self.postMessage({type: "log", text: "Ready!\n"});
    self.postMessage({type: "log_clean"});
    return pyodide;
})();


    start_text_spinner("Loading code... ");
    try {
        const code = `
import sys

import js
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

${await (await fetch("/projects/pet/RunningTextGifGenerator/resources/sandbox/gif.py")).text()}
${await (await fetch("/projects/pet/RunningTextGifGenerator/resources/sandbox/run_gif.py")).text()}


def print_progress_bar(x, y, name, start):
    if not x % 3 or x == y:
        return __print_progress_bar__(x, y, name, start)


__global_color_config = {
    "color_border": "#000000",
    "color_background": "#222222",
    "color_glare": "#666666",
    "color_pixel_off_light": "#880000",
    "color_pixel_off_dark": "#660000",
    "color_pixel_on_light": "#FF6666",
    "color_pixel_on_dark": "#FF0000",
}
`;
        await pyodide.runPythonAsync(code);
        stop_text_spinner();
    } catch (err) {
        self.postMessage({type: "stop_spinner"});
        self.postMessage({type: "log", text: "\n"+err.message});
        throw err;
    }

    self.postMessage({type: "log", text: "Ready!\n"});
    self.postMessage({type: "log_clean"});

    return pyodide;
})();




self.onmessage = async (event) => {
    const {type, code} = event.data;

    if (!["run", "stop"].includes(type)) {
        return;
    }

    const pyodide = await pyodideReadyPromise;

    self.postMessage({type: "gen_start"});

    try {
        let result = await pyodide.runPythonAsync(code);
        self.postMessage({type: "done", result});
    } catch (err) {
        self.postMessage({type: "log", text: err.message});
    }
    self.postMessage({type: "gen_stop"});
};

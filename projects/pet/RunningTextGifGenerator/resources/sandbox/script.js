let progressBar = true;

let spinnerTimer = null;
let spinnerIndex = 0;
const spinnerFrames = ["|", "/", "-", "\\"];

function startLogSpinner() {
    if (spinnerTimer) return;
    log_console.textContent += spinnerFrames[spinnerIndex];
    spinnerTimer = setInterval(() => {
        log_console.textContent = log_console.textContent.replace(/.$/, "");
        log_console.textContent += spinnerFrames[spinnerIndex];
        spinnerIndex = (spinnerIndex + 1) % spinnerFrames.length;
    }, 220);
}

function stopLogSpinner() {
    if (!spinnerTimer) return;
    clearInterval(spinnerTimer);
    spinnerTimer = null;
    spinnerIndex = 0;
    log_console.textContent = log_console.textContent.replace(/.$/, "");
}

let gif_code = null;
let run_gif_code = null;

async function loadScriptsOnce() {
    if (!gif_code) {
        gif_code = await (await fetch("resources/sandbox/gif.py")).text();
    }
    if (!run_gif_code) {
        run_gif_code = await (await fetch("resources/sandbox/run_gif.py")).text();
    }
    return {gif_code, run_gif_code};
}


let worker = null;
function createWorkerOnce() {
    if (worker) {
        return worker;
    }

    worker = new Worker("resources/sandbox/worker.js");
    worker.onmessage = (event) => {
        const {type, text, result, error} = event.data;

        if (type === "log" || type === "err") {
            if (type === "err") {
                if (log_console.style.display === "none") {
                    toggle_log.click();
                }
                log_console.style.display = "block";
                log_console.scrollIntoView();
                flashBorder(log_console, {count: 4, duration: 450});
            }

            if (text.includes("\r")) {
                const parts = text.split("\r");
                const last = parts.pop();
                const lines = log_console.textContent.split("\n");
                lines[lines.length - 1] = last.trimEnd();
                if (progressBar) {
                    updateProgressBar(last.trimEnd());
                }
                log_console.textContent = lines.join("\n");
                return;
            }

            // поддержка ESC-последовательности \x1b[{n}D
            const escRegex = /\x1b\[(\d+)D/;
            if (escRegex.test(text)) {
                const n = parseInt(text.match(escRegex)[1], 10);
                const clean = text.replace(escRegex, "");
                let content = log_console.textContent;
                // убираем n последних символов
                log_console.textContent = content.slice(0, -n) + clean;
                return;
            }
            log_console.textContent += text;
            log_console.scrollTop = log_console.scrollHeight;
        } else if (type === "done") {
            loader.style.display = "none";
            output_gif.style.display = "block";
            if (result) {
                output_gif.src = result;
            } else {
                output_gif.src = "";
            }
        } else if (type === "error") {
            loader.style.display = "none";
            output_gif.style.display = "block";
            //log_console.textContent += "❌ Ошибка: " + error + "\n";
        } else if (type === "start_spinner") {
            startLogSpinner();
        } else if (type === "stop_spinner") {
            stopLogSpinner();
        } else if (type === "log_clean") {
            log_console.textContent = "";
        }
    };

    return worker;
}

function escapeHTML(text) {
    const map = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;",
        "`": "&#96;",
        "/": "&#x2F;"
    };
    return text.replace(/[&<>"'/`]/g, function(match) {
        return map[match];
    });
}


// кнопка запуска
run_button.onclick = async () => {
    log_console.classList.remove("border_red");

    const worker = createWorkerOnce();
    output_gif.src = "";
    loader.style.display = "block";
    output_gif.style.display = "none";

    const {gif_code, run_gif_code} = await loadScriptsOnce();

    const fullCode = `
${gif_code}
${run_gif_code}

__print_progress_bar = print_progress_bar
print_progress_bar = lambda x, y, name, start: __print_progress_bar(x, y, name, start) if not x % 3 or x == y else None

__global_color_config = {
    "color_border": "#000000",
    "color_background": "#222222",
    "color_glare": "#666666",
    "color_pixel_off_light": "#880000",
    "color_pixel_off_dark": "#660000",
    "color_pixel_on_light": "#FF6666",
    "color_pixel_on_dark": "#FF0000",
}
global_color_config.update({
    "color_border": "${settings_color_border.value}",
    "color_background": "${settings_color_background.value}",
    "color_glare": "${settings_color_glare.value}",
    "color_pixel_off_light": "${settings_color_pixel_off_light.value}",
    "color_pixel_off_dark": "${settings_color_pixel_off_dark.value}",
    "color_pixel_on_light": "${settings_color_pixel_on_light.value}",
    "color_pixel_on_dark": "${settings_color_pixel_on_dark.value}",
})


running_text_gif_json('''${json_input.value}''', ${settings_columns.value}, ${settings_rows.value})
`;

    worker.postMessage({type: "run", code: fullCode});
};





function updateProgressBar(logLine) {
    // [███████████████                                   ][ 45/149 frames][ 30%][ 1.99s][export.git]
    const regex = /\[[█ ]+\]\[\s*(\d+)\/(\d+) frames\]\[\s*(\d+)%\]\[\s*(\d+\.\d+)s\]\[export\.git\]/;
    const match = logLine.match(regex);
    if (!match) return;

    const frames_done = format(parseFloat(match[1]).toString(), 3);
    const frames_all = format(parseFloat(match[2]).toString(), 3);
    const percent = format(parseFloat(match[3]).toString(), 3);
    const timeSec = format(parseFloat(match[4]).toFixed(2), 5);

    function format(text, length=1) {
        if (text.length >= length) {
            return text;
        }
        return " ".repeat(length - text.length) + text;
    }

    progress_bar.style.width = percent + "%";
    let content = `${frames_done}/${frames_all} ${percent}% ${timeSec}s`;
    progress_bar_data.innerHTML = `<pre>${escapeHTML(content)}</pre>`
}


toggle_log.addEventListener("click", function() {
    const isActive = this.classList.toggle("active");
    const newValue = isActive ? "true" : "false";
    if (isActive) {
        log_console.style.display = "block";
    } else {
        log_console.style.display = "none";
    }
});

// TODO remove
function flashBorder(el, { count = 4, duration = 500 } = {}) {
    // перезапуск, если класс уже висит
    el.classList.remove("border_flash");
    // форсим рефлоу, чтобы анимация стартовала заново
    void el.offsetWidth;

    el.style.setProperty("--flash-count", count);
    el.style.setProperty("--flash-duration", `${duration}ms`);
    el.classList.add("border_flash");

    // после последней итерации оставляем стабильный красный бордер
    const onEnd = () => {
      el.classList.remove("border_flash");
      el.classList.add("border_red");
      el.removeEventListener("animationend", onEnd);
    };
    el.addEventListener("animationend", onEnd);
}

document.querySelectorAll(".category_button").forEach(function(button) {
    button.addEventListener("click", function() {
        event.stopPropagation();
        this.nextElementSibling.classList.toggle("hidden");
    });
});





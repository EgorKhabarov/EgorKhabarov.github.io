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
                    console_toggle.click();
                }
                log_console.style.display = "block";
                log_console.scrollIntoView();
                log_console.classList.add("border_red");
                loader.style.display = "none";
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

            // Поддержка ESC-последовательности \x1b[{n}D
            const escRegex = /\x1b\[(\d+)D/;
            if (escRegex.test(text)) {
                const n = parseInt(text.match(escRegex)[1], 10);
                const clean = text.replace(escRegex, "");
                let content = log_console.textContent;
                // Убираем n последних символов
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
        } else if (type === "start_spinner") {
            startLogSpinner();
        } else if (type === "stop_spinner") {
            stopLogSpinner();
        } else if (type === "log_clean") {
            log_console.textContent = "";
        } else if (type === "gen_start") {
            run_button.style.display = "none";
            stop_button.style.display = "block";
            run_button.onclick = run_button_onclick;
        } else if (type === "gen_stop") {
            run_button.style.display = "block";
            stop_button.style.display = "none";
            stop_button.onclick = stop_button_onclick;
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
    run_button.onclick = null;
    log_console.classList.remove("border_red");

    const worker = createWorkerOnce();
    output_gif.src = "";
    loader.style.display = "block";
    output_gif.style.display = "none";

    const fullCode = `
global_color_config.update({
    "color_border": "${settings_color_border.value}",
    "color_background": "${settings_color_background.value}",
    "color_glare": "${settings_color_glare.value}",
    "color_pixel_off_light": "${settings_color_pixel_off_light.value}",
    "color_pixel_off_dark": "${settings_color_pixel_off_dark.value}",
    "color_pixel_on_light": "${settings_color_pixel_on_light.value}",
    "color_pixel_on_dark": "${settings_color_pixel_on_dark.value}",
})

running_text_gif_json(
    '''${json_input.value}''',
    ${settings_columns.value},
    ${settings_rows.value},
    ${settings_loop.value},
)
`;

    console.log(`GIF(columns=${settings_columns.value}, rows=${settings_rows.value}, loop=${settings_loop.value})`);
    worker.postMessage({type: "run", code: fullCode});
};
stop_button.onclick = async () => {
    stop_button.onclick = null;
    worker.postMessage({type: "stop"});
};
run_button_onclick = run_button.onclick;
stop_button_onclick = stop_button.onclick;


function updateFramePreview() {

    let columns = parseInt(settings_columns.value);
    let rows = parseInt(settings_rows.value);

    if (
        columns < 1 || columns > 200
        || rows < 1 || rows > 200
    ) {
        frame_preview.innerHTML = "";
        frame_preview.textContent = "Sorry the image is too big";
        return;
    }


    function roundRect(x, y, width, height, radius) {
        ctx.beginPath();
        ctx.moveTo(x + radius, y);
        ctx.lineTo(x + width - radius, y);
        ctx.arcTo(x + width, y, x + width, y + radius, radius);
        ctx.lineTo(x + width, y + height - radius);
        ctx.arcTo(x + width, y + height, x + width - radius, y + height, radius);
        ctx.lineTo(x + radius, y + height);
        ctx.arcTo(x, y + height, x, y + height - radius, radius);
        ctx.lineTo(x, y + radius);
        ctx.arcTo(x, y, x + radius, y, radius);
        ctx.closePath();
    }
    function rounded_rectangle(x1, y1, x2, y2, radius, fill) {
        ctx.fillStyle = fill;
        roundRect(x1, y1, x2-x1, y2-y1, radius);
        ctx.fill();
    }
    function rectangle(x1, y1, x2, y2, fill) {
        ctx.fillStyle = fill;
        ctx.fillRect(x1, y1, x2-x1, y2-y1);
    }
    function line(x1, y1, x2, y2, fill) {
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);

        ctx.strokeStyle = fill;
        ctx.lineWidth = 1;
        ctx.stroke();
    }

    let columns_pixels = columns * 2 + columns + 2 + 5 + 6;
    let rows_pixels = rows * 2 + rows + 3 + 5 + 5;

    color_config = {
        color_border: settings_color_border.value,
        color_background: settings_color_background.value,
        color_glare: settings_color_glare.value,
        color_pixel_off_light: settings_color_pixel_off_light.value,
        color_pixel_off_dark: settings_color_pixel_off_dark.value,
        color_pixel_on_light: settings_color_pixel_on_light.value,
        color_pixel_on_dark: settings_color_pixel_on_dark.value,
    };

    const canvas = document.createElement("canvas");
    canvas.width = columns_pixels-1;
    canvas.height = rows_pixels-1;
    const ctx = canvas.getContext("2d");

    //...

    rounded_rectangle(0, 0, columns_pixels - 1, rows_pixels - 1, radius=7, fill=color_config["color_border"]);
    rectangle(5, 5, columns_pixels - 6, rows_pixels - 6, color_config["color_background"]);
    line(6, rows_pixels - 6+0.5, columns_pixels - 7+1, rows_pixels - 6+0.5, color_config["color_glare"]);
    line(columns_pixels - 6+0.5, 6-0.5, columns_pixels - 6+0.5, rows_pixels - 7+1, color_config["color_glare"]);

    function func(c, r) {
        const pixels = [
            "                ",
            " #   #   #     #",
            " #   #         #",
            " #####  ##     #",
            " #   #   #     #",
            " #   #   #     #",
            " #   #   #      ",
            " #   #    ##   #",
            "                ",
        ];
        try {
            return pixels[r][c] == "#";  // c%2==0 && r%2==0;
        } catch (e) {}
    }

    for (let column = 0; column < columns; column++) {
        for (let row = 0; row < rows; row++) {
            let is_on = func(column, row);
            let start_pixel_column = 8 + (column * 2) + column - 1;
            let start_pixel_row = 8 + (row * 2) + row - 1;
            let string_is_on = is_on ? "on" : "off";
            let color_dark_pixel = color_config[`color_pixel_${string_is_on}_dark`];
            let color_light_pixel = color_config[`color_pixel_${string_is_on}_light`];

            rectangle(
                start_pixel_column,
                start_pixel_row,
                start_pixel_column + 2,
                start_pixel_row + 2,
                color_dark_pixel,
            );

            rectangle(
                start_pixel_column,
                start_pixel_row,
                start_pixel_column+1,
                start_pixel_row+1,
                color_light_pixel,
            );
        }
    }


    //...


    const img = document.createElement("img");
    img.src = canvas.toDataURL("image/png");
    img.style.imageRendering = "pixelated";
    img.width = canvas.width*2;
    img.height = canvas.height*2;

    frame_preview.innerHTML = "";
    frame_preview.appendChild(img);

}



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


console_toggle.addEventListener("click", function() {
    if (console_toggle.textContent === "Show Console") {
        console_toggle.textContent = "Hide Console";
        log_console.style.display = "block";
    } else {
        console_toggle.textContent = "Show Console";
        log_console.style.display = "none";
    }
});
updateFramePreview();


document.querySelectorAll(".category_button").forEach(function(button) {
    button.addEventListener("click", function() {
        event.stopPropagation();
        this.nextElementSibling.classList.toggle("hidden");
    });
});

document.addEventListener("DOMContentLoaded", function() {
    document.documentElement.scrollTop = 0;
})




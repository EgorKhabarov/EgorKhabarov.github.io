function loadExperimentalSettings() {
    const experimental_settings = localStorage.getItem("experimental_settings");
    const es = experimental_settings ? JSON.parse(experimental_settings) : {
        "experimental_updated_search": false,
        "experimental_font_size": 12,
    };
    if (es.experimental_updated_search === undefined) {
        es.experimental_updated_search = false;
    }
    if (es.experimental_font_size === undefined) {
        es.experimental_font_size = 12;
    }
    return es;
}
function saveExperimentalSettings() {
    localStorage.setItem(
        "experimental_settings",
        JSON.stringify(experimental_settings)
    );
}

function addExperimentalSettingCheckBox(group, setting_id, text, default_value, func) {
    const checkbox_container = document.createElement("div");
    checkbox_container.classList.add("checkbox_container");

    const label1 = document.createElement("label");
    label1.classList.add("toggle_switch");
    checkbox_container.appendChild(label1);

    const input = document.createElement("input");
    input.type = "checkbox";
    input.id = `${setting_id}_input`;
    input.checked = default_value;
    label1.appendChild(input);

    const span = document.createElement("span");
    span.classList.add("slider");
    label1.appendChild(span);

    const label2 = document.createElement("label");
    label2.setAttribute("for", `${setting_id}_input`);
    label2.textContent = text;
    checkbox_container.appendChild(label2);

    group.appendChild(checkbox_container);
    func(input.checked);
    input.addEventListener("change", () => {
        const value = input.checked;
        experimental_settings[setting_id] = value;
        saveExperimentalSettings();
        func(value);
    });
    return checkbox_container;
}
function addExperimentalSettingRange(group, setting_id, min, max, step, default_value, text, func, functype) {
    const checkbox_container = document.createElement("div");
    checkbox_container.classList.add("checkbox_container");

    const input = document.createElement("input");
    input.type = "range";
    input.min = min;
    input.max = max;
    input.step = step;
    input.value = default_value;
    input.id = `${setting_id}_input`;
    checkbox_container.appendChild(input);

    const label = document.createElement("label");
    label.setAttribute("for", `${setting_id}_input`);
    label.textContent = text;
    label.id = `${setting_id}_label`;
    checkbox_container.appendChild(label);

    group.appendChild(checkbox_container);
    func(input.value);
    if (functype === "input") {
        input.addEventListener("input", (event) => {
            const value = event.target.value;
            experimental_settings[setting_id] = value;
            saveExperimentalSettings();
            func(value);
        });
    } else if (functype === "change" || undefined) {
        input.addEventListener("change", () => {
            const value = input.value;
            experimental_settings[setting_id] = value;
            saveExperimentalSettings();
            func(value);
        });
    }
    return checkbox_container;
}

function addExperimentalSettingsGroup(page, name, description) {
    const group = document.createElement("div");
    group.classList.add("setting_group");

    if (name) {
        const nameEl = document.createElement("span");
        nameEl.classList.add("setting_label");
        nameEl.textContent = name;
        group.appendChild(nameEl);
    }
    if (description) {
        const descriptionEl = document.createElement("span");
        descriptionEl.classList.add("setting_description");
        descriptionEl.textContent = description;
        group.appendChild(descriptionEl);
    }
    page.appendChild(group);
    return group;
}
function fillExperimentalSettings(id, settings_map) {
    const page_experimental = document.getElementById(id);
    page_experimental.innerHTML = "";

    for (let [group_name, data] of Object.entries(settings_map)) {
        const group = addExperimentalSettingsGroup(page_experimental, group_name, data.description);
        for (let [setting_id, setting] of Object.entries(data.settings_map)) {
            if (setting.pre_func) {
                setting.pre_func();
            }
            if (setting.type === "checkbox") {
                addExperimentalSettingCheckBox(
                    group,
                    setting_id,
                    setting.label,
                    experimental_settings[setting_id],
                    setting.func,
                );
            } else if (setting.type === "range") {
                addExperimentalSettingRange(
                    group,
                    setting_id,
                    setting.min,
                    setting.max,
                    setting.step,
                    experimental_settings[setting_id],
                    setting.label,
                    setting.func,
                    setting.functype,
                );
            }
        }
    }
}

function genExperimentalSettingCheckBoxStyle(setting_id, label, styles) {
    return {
        "label": label,
        "type": "checkbox",
        "pre_func": () => {
            const style = document.createElement("style");
            style.id = `${setting_id}_style`;
            document.head.appendChild(style);
        },
        "func": (value) => {
            const style = document.getElementById(`${setting_id}_style`);
            style.textContent = value ? styles : "";
        },
    }
}
function genExperimentalSettingRangeStyle(setting_id, label, styles_func) {
    return {
        "label": label,
        "type": "range",
        "min": "8",
        "max": "20",
        "step": "2",
        "functype": "input",
        "pre_func": () => {
            const style = document.createElement("style");
            style.id = `${setting_id}_style`;
            document.head.appendChild(style);
        },
        "func": (value) => {
            const style = document.getElementById(`${setting_id}_style`);
            if (value) {
                style.textContent = styles_func(value);
            } else {
                style.textContent = "";
            }
            const label_element = document.getElementById(`${setting_id}_label`);
            label_element.textContent = label + ` ${value}`;
        },
    }
}

const experimental_settings = loadExperimentalSettings();
fillExperimentalSettings("page_experimental", {
    "Search": {
        "description": "",
        "settings_map": {
            "experimental_updated_search": genExperimentalSettingCheckBoxStyle(
                setting_id="experimental_updated_search",
                label="The cheat sheet search is located differently",
                styles=`
#page_search_container {
    position: static;
    padding: 0px;
    box-shadow: none;
    border-radius: 0px;
    width: 100%;
    gap: 0px;
    border: 0px;
    border-bottom: 1px solid var(--border-color);
}
#page_search_input {
    border-radius: 0px;
    background-color: var(--hover-color);
}
.page_search_buttons {
    padding: 4px 0px;
    margin-right: 6px;
}
.page_search_button {
    padding: 2px 3px;
    width: 25px;
    height: 25px;
    border: 0px;
    background: inherit;
}
.page_search_button > svg {
    width: 100%;
    height: 100%;
}
#page_search_container > div:last-child {
    padding: 2.2px 4px;
    border-top: 1px solid var(--border-color);
}
.toc_header {
    padding: 18px;
}
`,
            ),
        },
    },
    "Settings": {
        "description": "",
        "settings_map": {
            "experimental_updated_settings": genExperimentalSettingCheckBoxStyle(
                setting_id="experimental_updated_settings",
                label="The settings on a mobile device look different",
                styles=`
@media (max-width: 768px) {
    .settings_layout {
        flex-direction: column;
    }
    .settings_sidebar {
        width: calc(100% - 45px);
    }
}
`,
            ),
        },
    },
    "Font": {
        "description": "",
        "settings_map": {
            "experimental_font_size": genExperimentalSettingRangeStyle(
                setting_id="experimental_font_size",
                label="Font size",
                styles_func=(value)=>`
.cheatsheet_field {
    font-size: ${value}px;
}
`,
            ),
        },
        "settings_map": {
            "experimental_font_size": {
                "label": "Font size",
                "type": "range",
                "min": "8",
                "max": "20",
                "step": "2",
                "functype": "input",
                "pre_func": () => {
                    const style = document.createElement("style");
                    style.id = `${setting_id}_style`;
                    document.head.appendChild(style);
                },
                "func": (value) => {
                    const style = document.getElementById(`${setting_id}_style`);
                    if (value) {
                        style.textContent = ((value) => `.cheatsheet_field {font-size: ${value}px;}`)(value);
                    } else {
                        style.textContent = "";
                    }
                    const label_element = document.getElementById(`${setting_id}_label`);
                    if (!label_element.dataset.text) {
                        label_element.dataset.text = label_element.textContent;
                    }
                    label_element.textContent = label_element.dataset.text + ` ${value}`;
                    label_element.style.fontSize = `${value}px`;
                },
            },
        },
    },
});

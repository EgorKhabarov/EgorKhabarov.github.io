function loadExperimentalSettings() {
    const experimental_settings = localStorage.getItem("experimental_settings");
    const es = experimental_settings ? JSON.parse(experimental_settings) : {
        "experimental_updated_search": false,
    };
    if (es.experimental_updated_search === undefined) {
        es.experimental_updated_search = false;
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
    input.id = setting_id;
    input.checked = default_value;
    label1.appendChild(input);

    const span = document.createElement("span");
    span.classList.add("slider");
    label1.appendChild(span);

    const label2 = document.createElement("label");
    label2.setAttribute("for", setting_id);
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
        const search_group = addExperimentalSettingsGroup(page_experimental, group_name, data.description);
        for (let [setting_id, setting] of Object.entries(data.settings_map)) {
            if (setting.pre_func) {
                setting.pre_func();
            }
            if (setting.type === "bool") {
                addExperimentalSettingCheckBox(
                    search_group,
                    setting_id,
                    setting.label,
                    experimental_settings[setting_id],
                    setting.func,
                );
            }
        }
    }
}

const experimental_settings = loadExperimentalSettings();
fillExperimentalSettings("page_experimental", {
    "Search": {
        "description": "",
        "settings_map": {
            "experimental_updated_search": {
                "label": "The cheat sheet search is located differently",
                "type": "bool",
                "pre_func": () => {
                    const style = document.createElement("style");
                    style.id = "experimental_updated_search_styles";
                    document.head.appendChild(style);
                },
                "func": (value) => {
                    if (value) {
                        experimental_updated_search_styles.textContent = `
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
}
.toc_header {
    padding: 18px;
}
`;
                    } else {
                        experimental_updated_search_styles.textContent = "";
                    }
                },
            },
        },
    },
});


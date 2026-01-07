
/* Copy Download Code */
function copy(text) {
    const textarea = document.createElement("textarea");
    document.body.appendChild(textarea);
    textarea.value = text;
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
}
function CopyCode(button_element) {
    let code_element = button_element.parentElement.parentElement.lastElementChild;

    const pre_element = document.createElement("pre");
    pre_element.innerHTML = code_element.innerHTML;
    if (!isCtrlPressed) {
        pre_element.querySelectorAll(".unselectable").forEach(
            element => element.remove()
        );
    }
    copy(pre_element.textContent);

    html1 = '<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#icon_code_done"/></svg><text class="unselectable">Copied!</text>';
    html2 = '<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#icon_code_copy"/></svg><text class="unselectable">Copy code</text>';

    button_element.innerHTML = html1;

    setTimeout(function() {
        button_element.innerHTML = html2;
    }, 1000);
}
function DownloadCode(button_element, filename) {
    code_element = button_element.parentElement.parentElement.lastElementChild;

    text = code_element.textContent;//.split("\n").slice(1).join("\n");
    const element = document.createElement("a");
    element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
    element.setAttribute("download", filename);
    element.style.display = "none";
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);

    download_html = `<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#icon_code_download"/></svg><text class="unselectable" title="${filename}">Download code</text>`;
    downloaded_html = `<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#icon_code_done"/></svg><text class="unselectable" title="${filename}">Download!</text>`;

    button_element.innerHTML = downloaded_html;

    setTimeout(function() {
        button_element.innerHTML = download_html;
    }, 1000);
}
let isCtrlPressed = false;
document.addEventListener("keydown", function(event) {if (event.ctrlKey) {isCtrlPressed = true;}});
document.addEventListener("keyup", function(event) {if (!event.ctrlKey) {isCtrlPressed = false;}});
document.addEventListener("click", function(event) {
    if (event.target.tagName === "CODE") {
        if (event.target.classList.contains("code_no_copy")) {
            return;
        }
        const temp = document.createElement("input");
        document.body.appendChild(temp);
        temp.value = event.target.textContent;
        temp.select();
        document.execCommand("copy");
        document.body.removeChild(temp);
    }
});

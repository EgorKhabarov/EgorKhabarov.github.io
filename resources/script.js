document.addEventListener("click", function(event) {
    if (event.target.tagName === "CODE" && event.target.classList.contains("copy")) {
        const tempInput = document.createElement("input");
        document.body.appendChild(tempInput);
        tempInput.value = event.target.textContent;
        tempInput.select();
        document.execCommand("copy");
        document.body.removeChild(tempInput);
    }
});

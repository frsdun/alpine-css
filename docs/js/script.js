function connectBackModeToUi() {
    const darkModeLink = document.querySelector("#js-dark-mode");
    darkModeLink.addEventListener("click", () => {
        const body = document.querySelector("body");
        if (body.classList.contains("dark-mode")) {
            body.classList.remove("dark-mode");
            localStorage.removeItem("darkMode");
        } else {
            body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "dark-mode");
        }
    });
}

function lookForDarkModePreference() {
    const pref = localStorage.getItem("darkMode");
    if (pref === "dark-mode") {
        const body = document.querySelector("body");
        body.classList.add("dark-mode");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    connectBackModeToUi();
    lookForDarkModePreference();
});

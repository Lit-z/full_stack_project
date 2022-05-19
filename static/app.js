// function for toggling a different colour scheme (in this case a dark mode)
// mainBox is for setting variables in js based on class names in the html
// button is used for determining the text that appears on the button 'light or 
// dark mode' to indicate it will change to the opposite theme
function darkMode() {
    let element = document.body;
    let mainBox = document.getElementsByClassName("main-body");
    let state = localStorage.getItem("state");
    let button = document.getElementById("mode-button");

// dark-mode, dark-modeb refer to diff sections in css for being able to set 
// different colours/ themes/ styles on different parts (js variables from 
// the html classes above)
    element.classList.toggle("dark-mode");
    for (const box of mainBox) {
        box.classList.toggle("dark-modeb");
    }

// checks the state (the last variable set at the top) of the current theme
// to store this information in local storage, to remember the user setting
// this updates everytime the user presses the dark mode button
    if (state !=="dark") {
        localStorage.setItem("state", "dark");
        button.textContent='Light Mode';
    } else {
        localStorage.setItem("state", "light");
        button.textContent='Dark Mode';
    }
}

// similar code to above in this case, it's now checking for if there is state
// in the local storage through .getItem()
function darkCheck() {
    let element = document.body;
    let mainBox = document.getElementsByClassName("main-body");
    let state = localStorage.getItem("state");
    let button = document.getElementById("mode-button");

    if (state =="dark") {
        element.classList.toggle("dark-mode");
        button.textContent='Light Mode';

        for (const box of mainBox) {
            box.classList.toggle("dark-modeb");
        }

    } else {
        button.textContent='Dark Mode';
    }
}

// date display function (on admin page for fun)
function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}
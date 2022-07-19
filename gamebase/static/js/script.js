/* jshint esversion: 11 */

/*
    jQuery for MaterializeCSS initialization
*/

document.addEventListener("DOMContentLoaded", function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    // collapsible initializataion
    let collapsibles = document.querySelectorAll(".collapsible");
    M.Collapsible.init(collapsibles);

    // datepicker initialization
    let datepickers = document.querySelectorAll(".datepicker");
    const d = new Date();
    let year = d.getFullYear();


    M.Datepicker.init(datepickers, {
        selectMonths: true,
        selectYears: true,
        yearRange: [1970, year + 5],
        close: "Ok",
        closeOnSelect: false,
    });

    // modal initializataion
    let modals = document.querySelectorAll(".modal");
    M.Modal.init(modals);
});


function requiredGenre() {
    document.getElementById('required-genre').style.cssText = 'color: #F44336;';
}

// Stop keyboard input on date field
function preventKeyboardInput(event) {
    event.preventDefault();
  }
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

document.querySelector(document).ready(function() {
    document.querySelector("select").material_select();

    // for HTML5 "required" attribute
    document.querySelector("select[required]").css({
        display: 'inline',
        position: 'absolute',
        float: 'left',
        padding: 0,
        margin: 0,
        border: '1px solid rgba(255,255,255,0)',
        height: 0, 
        width: 0,
        top: '2em',
        left: '3em',
        opacity: 0,
        pointerEvents: 'none'
      });
});

function requiredGenre() {
    document.getElementById('required-genre').style.cssText = 'color: #F44336;';
}
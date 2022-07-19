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


// Stop keyboard input on date field
function preventKeyboardInput(event) {
    event.preventDefault();
  }


// Workaround for select validation styling
document.addEventListener("DOMContentLoaded", function () {
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = "border-bottom: 1px solid #4caf50; box-shadow: 0 1px 0 0 #4caf50;";
        let classInvalid = "border-bottom: 1px solid #f44336; box-shadow: 0 1px 0 0 #f44336;";
        let selectValidate = document.querySelector("select.validate");
        let selectWrapperInput = document.querySelector(".select-wrapper input.select-dropdown");
        if (selectValidate.hasAttribute("required")) {
            selectValidate.style.cssText = "display: block; height: 0; padding: 0; width: 0; position: absolute;";
        }
        selectWrapperInput.addEventListener("focusin", (e) => {
            e.target.parentNode.addEventListener("change", () => {
                ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
                for (let i = 0; i < ulSelectOptions.length; i++) {
                    if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled") {
                        e.target.style.cssText = classValid;
                    }
                }
            });
        });
        selectWrapperInput.addEventListener("click", (e) => {
            ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
            for (let i = 0; i < ulSelectOptions.length; i++) {
                if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled" && ulSelectOptions[i].style.backgroundColor == "rgba(0, 0, 0, 0.03)") {
                    e.target.style.cssText = classValid;
                } else {
                    e.target.addEventListener("focusout", () => {
                        if (e.target.parentNode.childNodes[3].hasAttribute("required")) {
                            if (e.target.style.borderBottom != "1px solid rgb(76, 175, 80)") {
                                e.target.style.cssText = classInvalid;
                            }
                        }
                    });
                }
            }
        });
    }
});

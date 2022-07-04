/*
    jQuery for MaterializeCSS initialization
*/

// select initialization
let selects = document.querySelectorAll("select");
M.FormSelect.init(selects);

$(document).ready(function(){
    $('select').formSelect();
  });
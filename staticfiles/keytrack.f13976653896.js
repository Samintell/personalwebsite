var textData = "";
$(document).ready(function () {
    textData = $("#hiddenData").val();
    var lastDate = new Date();
    $(".track").keydown(function (event) {
        var curDate = new Date();
        //console.log(event);
        //console.log(event.which);
        textData += "" + (curDate - lastDate) + ":d" + event.which + "|"; // format "ms:(u/d)keycode|"
        lastDate = curDate;
    });
    $(".track").keyup(function (event) {
        var curDate = new Date();
        //console.log(event);
        //console.log(event.which);
        textData += "" + (curDate - lastDate) + ":u" + event.which + "|";
        lastDate = curDate;
    });

    $("form").submit(function (event) {
        if (($('#q1').val() + $('#q2').val() + $('#q3').val()).length < 300) {
            event.preventDefault();
            $('#error').val("Not Enough Characters. A minimum of 300 characters is required").show();
        }
        $("#hiddenData").val(textData);
    });
});
// $("#edit_link").change(function() {
//     if ($("#edit_field").show()) {
// } else {
//         $("#edit_field").hide();
//     };
// });
//     $("#edit_link").trigger("change");

$(document).ready(function(){
    $(".edit_field").hide();

$(".edit_button").click(function() {
    $(this).show();
    $(".edit_field").toggle();
    });
});
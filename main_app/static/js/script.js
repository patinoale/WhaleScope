$(document).ready(function(){
    $(".edit_field").hide();

$(".edit_button").click(function() {
    const id =  $(this)['0'].id.split('_')[2]
    $(`#edit_field_${id}`).toggle();
    });
});


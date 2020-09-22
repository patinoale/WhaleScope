$(document).ready(function(){
    $(".edit_field").hide();
    $(".reply_form").hide();

$(".edit_button").click(function() {
    const id =  $(this)['0'].id.split('_')[2]
    $(`#edit_field_${id}`).toggle();
    });

    $(".reply_button").click(function() {
      const replyid =  $(this)['0'].id.split('_')[2]
      $(`#reply_form_${replyid}`).toggle();
      });
});

twttr.widgets.createTimeline(
    {
      sourceType: "list",
      ownerScreenName: "Underwatertimes",
      slug: "underwater-news"
    },
    document.getElementById("twitter")
  );


$(document).ready(function(){
    $(".edit_field").hide();

$(".edit_button").click(function() {
    const id =  $(this)['0'].id.split('_')[2]
    $(`#edit_field_${id}`).toggle();
    });
});

// $(document).ready(function(){
//     $('.likes').css('color', 'lightgrey');

// $('.likes').click(function(){
    
//     $('#likes').toggleClass('clicked');
// })
// })

twttr.widgets.createTimeline(
    {
      sourceType: "list",
      ownerScreenName: "Underwatertimes",
      slug: "underwater-news"
    },
    document.getElementById("twitter")
  );

//   #C0FDFF `#likes_${likeid}` const likeid = $(this)['0'].likeid.split('_')[2]
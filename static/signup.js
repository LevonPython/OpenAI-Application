$(function() {
  // This code runs when the document is ready

  setTimeout(function() {
    // This code runs after 5 seconds

    $(".message_flash").fadeOut(3000);
    // Hide the element with class "message_flash" using a blind effect
    // with a duration of 3 seconds
  }, 4000);
  // Wait for 4 seconds before executing the code inside the setTimeout function
})


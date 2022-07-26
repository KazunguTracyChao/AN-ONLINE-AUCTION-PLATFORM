if (document.readyState == "loading") {
  document.addEventListener("DOMContentLoaded", ready);
} else {
  ready();
}
// $(window).load(function() {
//   $(".loader").fadeOut("slow");
// });

function ready() {
  console.log("doc ready");
  $(".loader").fadeOut("slow");
}

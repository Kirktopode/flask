// client-side js
// run by the browser each time your view template is loaded

// by default, you've got jQuery,
// add other scripts at the bottom of index.html

$(function() {
  $('form').submit(function(event) {
    event.preventDefault();
    var time = $('input').val();
    console.log(time);
    time = time.replace(/ /g, "_").replace(/\//g,"-");
    console.log(time);
    window.location.href += "api/time/" + time;
  });

});

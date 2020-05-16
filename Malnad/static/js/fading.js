/**
 * Created by MyPc on 13-05-2020.
 */

$(function () {

  var showText = ["Unique-Design","Responsive View",
  "Flexibility","User Friendly","Online Support","Trusted Product"];

  var
    showNum = 0,
    $showText = $('.showtext');

  function doShow() {
    $showText.text(showText[showNum]);
    // $showText.fadeIn('slow', function () {
    //   $showText.fadeOut('slow', function () {

      $showText.fadeIn(1500, function () {
      $showText.fadeOut(1500, function () {
        //lets make it so it wraps back to the start
        showNum = (showNum + 1) % showText.length;
        doShow();
      });
    });

  }

  doShow();
});

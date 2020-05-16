/**
 * Created by MyPc on 12-05-2020.
 */
$(function () {
    $(".left.pane").resizable({
        handles: "e, w"
    });
    $(".right.pane").resizable({
        handles: "e, w"
    });
    $(".center.pane .inner .bottom").resizable({
        handles: "n, s"
    });
});
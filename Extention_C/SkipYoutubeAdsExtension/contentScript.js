var count = 0;
var observer = new MutationObserver(function (mutations) {
    if ($(".button-inner") != null && count == 0) {
        $(".button-inner").click(function () {
            alert("Clicked");
        });
        $(".button-inner").on("click").delay(1000);
        count += 1;
    }

});
observer.observe(document, { attributes: false, childList: true, characterData: false, subtree: true });

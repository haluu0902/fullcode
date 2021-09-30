// ==UserScript==

// @name BC.Game

// @namespace http://tampermonkey.net/

// @version 188

// @description iiNt3LiiGrab

// @author ][NT3L][G3NC][

// @match https://bc.game/*

// @match https://nanogames.io/*

// @grant none

// ==/UserScript==

var isLose = false;
var last = 0
var loseStreak = 0


function doThings() {


    clearInterval(theShit);

    var theLength1 = document.getElementsByClassName("item-wrap is-lose").length - 1;
    var theLength2 = document.getElementsByClassName("recent-item").length - 1;

    // For Loop Thru And Click Any Coin Drops Up For Grabs!

    for (var i = theLength1; i >= 0; i--) {

        // Get Coin Drop Status

        console.log(document.getElementsByClassName("item-wrap is-lose")[theLength1].innerText);
        
        var text1 = document.getElementsByClassName("item-wrap is-lose")[theLength1].innerText;
        var text2 = document.getElementsByClassName("recent-item")[theLength2].innerText;
        if (last != text2) {
            last = text2
            if (text1 == text2) {
                isLose = true;
                loseStreak += 1
            }
            else {
                loseStreak = 0
            }
        }

    }

    if (isLose) {

        isLose = false;

        setTimeout(doThings, 500);
        if (loseStreak >= 20) {
            document.getElementsByClassName("no-select")[0].click()
        }
        if (loseStreak >= 30) {
            document.getElementById("set_seed").click()
            document.getElementsByClassName("button-inner")[2].click()
            loseStreak = 0
        }

    } else {

        setTimeout(doThings, 500);

    }

}

var theShit = setInterval(doThings, 5000);
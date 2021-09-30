// ==UserScript==

// @name BC.Game Change Hilow and Seed

// @namespace http://tampermonkey.net/

// @version 188

// @description Change Hilow and Sed

// @author Savior XXI

// @match https://bc.game/*

// @grant none

// ==/UserScript==

var isLose = false;
var last = 0
var loseStreak = 0
var count = 0
var i =0
var textHilo = "Low"

function getTime(){
    var current = new Date();
    return current.getHours()+":"+current.getMinutes();
}


function doThings() {


    clearInterval(theShit);

    var theLength1 = document.getElementsByClassName("item-wrap is-lose").length - 1;
    var theLength2 = document.getElementsByClassName("recent-item").length - 1;

    for (i = theLength1; i >= 0; i--) {


        
        console.log(count + "--" + loseStreak);
        var text1 = document.getElementsByClassName("item-wrap is-lose")[theLength1].innerText;
        var text2 = document.getElementsByClassName("recent-item")[theLength2].innerText;
        if (last != text2) {
            last = text2;
            count += 1;
            if (text1 == text2) {
                isLose = true;
                loseStreak += 1;
            }
            else {
                loseStreak = 0;
            }
        }

    }

    if (isLose) {

        isLose = false;

        
        if (loseStreak == 20) {
            document.getElementsByClassName("no-select")[0].click();
            console.log(getTime()+"---"+"Change High Low");
        }
        if (loseStreak >= 30 || count == 500) {
            document.getElementById("set_seed").click();
            for (i = 10; i >= 0; i--) {
                try{
                    if(document.getElementsByClassName("button-inner")[i].innerText == "Use New Seeds"){
                        try{
                            document.getElementsByClassName("button-inner")[i].click();    
                        }
                        catch{
                            document.getElementsByClassName("button-inner")[i].click();   
                        }
                        console.log(getTime()+"---"+"Change High Low");
                    }
                }
                catch(e){

                }
            }
            
            loseStreak = 0;
            count = 0
            console.log(getTime()+"---"+"Change Seed");
        }
        setTimeout(doThings, 500);

    } else {

        setTimeout(doThings, 500);

    }

}

var theShit = setInterval(doThings, 5000);
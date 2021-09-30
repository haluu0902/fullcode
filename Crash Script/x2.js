var config = {
    bet: { label: 'Bet', value: 10, type: 'number' },
    payout: { label: 'Payout', value: 2, type: 'number' },
    sleepSettingTitle: { label: "Sleep setting", type: "title" },
    sleepAfter: { label: 'Sleep after losing: ', value: 4, type: 'number' },
    sleepMin: { label: 'Sleep min', value: 10, type: 'number' },
    sleepMax: { label: 'Sleep max', value: 20, type: 'number' },
    onLoseTitle: { label: "On lose", type: "title" },
    onLose: { label: 'Multiply the bet: ', value: 2, type: 'number' },
    //onWinTitle: { label: "On win", type: "title" },
    //onWin: { label: 'Multiply the bet: ', value: 1, type: 'number' },
    stopSettingTitle: { label: "Stop setting", type: "title" },
    takeProfit: { label: 'Take profit: ', value: 1000, type: 'number' },
    stopLoss: { label: 'Stop loss: ', value: 1000, type: 'number' },
    maxBet: { label: 'Stop if bet >', value: 500, type: 'number' },
}


function main() {
    log.info("Start");
    var bet = config.bet.value;
    var betSleep = currency.minAmount;
    var payout = config.payout.value;
    var sleepAfter = config.sleepAfter.value;
    var sleepMin = config.sleepMin.value;
    var sleepMax = config.sleepMax.value;
    var onLose = config.onLose.value;
    //var onWin = config.onWin.value;
    var takeProfit = config.takeProfit.value;
    var stopLoss = config.stopLoss.value;
    var maxBet = config.maxBet.value;
    var mainB = bet;
    //var mainP = payout;
    var loseS = 0;
    var Bbet = 0;
    var profit = 0;
    var sleep = 0;
    game.onBet = function () {
        game.bet(bet, payout).then(function (payout) {
            if (payout > 1) {
                profit += bet*(payout - 1);
                log.success("We won " + bet + ", payout " + payout + "X! " + "Profit: " + profit);
                if (sleep <= 0) {
                    if (loseS >= sleepAfter) {
                        bet = Bbet;
                    }
                    else {
                        bet = mainB;
                    }
                    loseS = 0;
                }
                else {
                    bet = betSleep;
                }

            } else {
                profit -= bet;
                log.error("We lost " + bet + ", payout " + payout + "X! " + "Profit: " + profit);
                loseS += 1;
                if (loseS >= sleepAfter || sleep > 0) {
                    if (loseS == sleepAfter) {
                        Bbet = bet * onLose;
                        sleep = Math.floor(Math.random() * (sleepMax - sleepMin + 1)) + sleepMin;
                        log.info("Random sleep: " + sleep + " time!");
                    }
                    bet = betSleep;
                }
                else {
                    bet = bet * onLose;
                }
            }
        });
        if(sleep > 0){
            log.info("Sleep: " + sleep + " left!");
        }
        if(sleep == 0 && loseS >= sleepAfter ){
            log.info("Sleep until win!");
        }
        sleep -= 1;        
        if (profit <= (-stopLoss) || profit >= takeProfit || bet >= maxBet) {
            game.stop();
        }
    }
}
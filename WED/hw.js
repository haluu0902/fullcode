var config = {
    bet: { label: 'bet', value: 10, type: 'number' },
    payout: { label: 'payout', value: 2, type: 'number' }
}


function main() {
    log.info("Start");
    var bet = config.bet.value;
    var payout = config.payout.value;
    var mainB = bet;
    var mainP = payout;
    var loseS = 0;
    var Bbet = 0;
    var profit = 0;
    var sleep = 0;
    game.onBet = function () {
        game.bet(bet, payout).then(function (payout) {
            if (payout > 1) {
                profit += bet;
                log.success("We won " + bet + ", payout " + payout + "X! " + "Profit: " + profit);
                if (sleep <= 0) {
                    if (loseS >= 4) {
                        bet = Bbet;
                    }
                    else {
                        bet = mainB;
                    }
                    loseS = 0;
                }
                else {
                    bet = currency.minAmount;
                }

            } else {
                profit -= bet;
                log.error("We lost " + bet + ", payout " + payout + "X! " + "Profit: " + profit);
                loseS += 1;
                if (loseS >= 4 || sleep > 0) {
                    if (loseS == 4) {
                        Bbet = bet * 2;
                        sleep = Math.floor(Math.random() * (20 - 10 + 1)) + 10;
                        log.info("Random sleep: " + sleep + " time!");
                    }
                    bet = currency.minAmount;
                }
                else {
                    bet = bet * 2;
                }
            }
        });
        if(sleep > 0){
            log.info("Sleep: " + sleep + " left!");
        }
        if(sleep == 0 && loseS >=4 ){
            log.info("Sleep until win!");
        }
        sleep -= 1;        
        if (profit <= mainB*(-4000) || profit >= mainB*4000) {
            game.stop();
        }
    }
}
var config = {
    donateTitle: { label: "Donate (TRX - USDT - BTT)", type: "title" },
    donateValue: { label: 'My TRC20 address', value: "TJLKaDdAdgJG1nnHaPYEeTozw2qTUBTYp4", type: 'number' },
    settingTitle: { label: "Setting", type: "title" },
    bet: { label: 'Bet', value: 0.0001, type: 'number' },
    payoutBigBet: {label:'Payout to big bet', value: 1.2, type: 'number'},
    payout1: { label: 'Payout from', value: 1.01, type: 'number' },
    payout2: { label: 'Payout to', value: 100, type: 'number' },
    payout3: { label: 'Payout from (to Big)', value: 90, type: 'number' },
    payout4: { label: 'Payout to (to Big)', value: 100, type: 'number' },
    betMax: { label: 'Bet Max', value: 1000000, type: 'number' },
    stopLost: { label: 'Stop Lost', value: 999, type: 'number' },
    takeProfit: { label: 'Take Profit', value: 999, type: 'number' }
}




function main() {
    log.info("Start");
    var bigBet = config.bet.value;
    var sleepBet = currency.minAmount;
    var bet = sleepBet;
    var payoutBigBet = config.payoutBigBet.value;
    var payout1 = config.payout1.value;
    var payout2 = config.payout2.value;
    var payout3 = config.payout3.value;
    var payout4 = config.payout4.value;
    var payout = 0;
    var betMax = config.betMax.value;
    var stopLost = config.stopLost.value;
    var takeProfit = config.takeProfit.value;
    var payoutB = 0;
    var mainB = bigBet;
    var loseS = 0;
    var winS = 0;
    var profit = 0;
    var winP = 0;
    var mainPayout = 0;
    var currentProfit = 0;
    var check = true;
    game.onBet = function () {
        payout = ((Math.random() * (payout2-payout1)*10)+payout1*10)/10;
        payout = Math.round(payout*100) / 100;
        if(payout <=payout4 && payout > payout3){
            payout = payoutBigBet
            bet = bigBet;
            check =true;
        }
        else{
            check = false;
            bet =sleepBet;
        }
        payoutB = payout;
        mainPayout=payout;
        log.info("Bet: " + bet + " - Payout: " + payout);
        game.bet(bet, payout).then(function (payout) {

            if (payout > 1) {
                winP = (bet * (payoutB - 1));
                profit += winP;
                currentProfit = 0
                log.success("We won " + winP + ", payout " + payout + "X! " + "Profit: " + Math.round(profit * 1000000) / 1000000);
                loseS = 0;
                if(check){
                    winS += 1;
                    if(bigBet * payoutBigBet < mainB*2){
                        bigBet = bigBet*payoutBigBet;
                    }      
                    else{
                        bigBet = mainB;
                        log.info("Resssssssssssss");
                    }                        
                }
                log.info("Win streak: " + winS + " time!");

            } else {
                lostP = bet
                profit -= lostP;
                currentProfit += lostP
                loseS += 1;
                if(check){
                    winS = 0;
                    bigBet = bigBet*(1/(payoutBigBet-1) + 1.01);
                }
                log.error("We lost " + lostP + ", payout " + payout + "X! " + "Profit: " + Math.round(profit * 1000000) / 1000000);
                log.info("Lose streak: " + loseS + " time!");
            }
        });
        if (profit <= stopLost*(-1) || profit >= takeProfit || bet >= betMax) {
            game.stop();
        }
    }
}
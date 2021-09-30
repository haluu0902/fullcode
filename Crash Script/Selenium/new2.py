import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
import time
import math
import re
import operator

timeStart = time.time()
timeRunSec = 0
minutes =0
seconds =0

lastPayout=0
payouting = 2
betMain = round(float(input("Bet: ")),4)
stopLost = round(float(input("Stop lost: ")),4)*(-1)
takeProfit = round(float(input("Take profit: ")),4)
print("Success bet: ", betMain)
bet = betMain
bet1 = betMain*4
bet2 = betMain
bet3 = betMain
bet4 = betMain
bet5 = betMain
maxBet = betMain
profit = 0.00
payout2 = 0.00
timeBet = 0
timeRun = 0
temporaryNext = ""
rs = open("./data/handingResult_18_7", "r")
dataRs = rs.readline()
rs.close()
url = "https://bc.game/crash"
driver = webdriver.Chrome("chromedriver.exe")

def getNext(arr):
    listReturnNum={"a" : 0, "b" : 0, "c": 0, "d": 0, "e" : 0, "f" : 0}
    temporaryRs = ""
    stringArr = ''.join(str(e) for e in arr)
    listResult = [_.start() for _ in re.finditer(stringArr, dataRs)]
    if(len(listResult) == 0):
        return "Null"
    else: 
        for vrs in listResult:
            try:
                temporaryRs = (dataRs[vrs + len(stringArr)])
            except:
                break
            if(temporaryRs == "a"):
                listReturnNum["a"] += 0
            elif(temporaryRs == "b"):
                listReturnNum["b"] += 1
            elif(temporaryRs == "c" or temporaryRs == "d"):
                listReturnNum["c"] += 1
            elif(temporaryRs == "e" or temporaryRs == "f" or temporaryRs == "g"):
                listReturnNum["d"] += 1
            elif(temporaryRs == "h" or temporaryRs == "i"):
                listReturnNum["e"] += 1
            else:
                listReturnNum["f"] += 1
        return max(listReturnNum, key=listReturnNum.get)
def handingNumber(value):
    if(value >= 1 and value < 2):
        return "a"
    elif(value >= 2 and value < 3):
        return "b"
    elif(value >= 3 and value < 4):
        return "c"
    elif(value >= 4 and value < 5):
        return "d"
    elif(value >= 5 and value < 6):
        return "e"
    elif(value >= 6 and value < 7):
        return "f"
    elif(value >= 7 and value < 8):
        return "g"
    elif(value >= 8 and value < 9):
        return "h"
    elif(value >= 9 and value < 10):
        return "i"
    else:
        return "k"


driver.get(url)
time.sleep(3)
a = input("Continue: ")
historyValue = [
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[3]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[4]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[5]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x","")))
]
payout = 0.00
inputB = driver.find_elements_by_xpath("""//*[@class="input-control"]/input[@type="text"]""")
while True:
    check = True
    payout = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x",""))
    if(lastPayout != payout):
        del historyValue[0]
        historyValue.append(handingNumber(payout))
        if(''.join(str(e) for e in historyValue)[3] == "a"):
            temporaryNext = "a"
        else:
            temporaryNext = getNext(historyValue)
        print("History: ", historyValue)
        print("Next Bet: ", temporaryNext)
        if(temporaryNext == "b"):
            payouting = round((payout - math.floor(payout)+1),2)
            bet = bet1
        elif(temporaryNext == "c"):
            payouting = 2
            bet = bet2
        elif(temporaryNext == "d"):
            payouting = 3
            bet = bet3
        elif(temporaryNext == "e"):
            payouting = 4
            bet = bet4
        elif(temporaryNext == "f"):
            payouting = 10
            bet = bet5
        else:
            print("Bet: 0 - Pass this time")
            check= False
        lastPayout = payout
        timeRun+=1
        print ("Last payout: ", lastPayout)
        if(check):
            timeBet += 1
            if(timeRun != 1):
                ActionChains(driver).click(inputB[0]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(str(bet)).perform()
                time.sleep(0.5)
                ActionChains(driver).click(inputB[1]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(str(payouting)).perform()
                time.sleep(2)
                try:
                    betBut = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/button/div").click()
                except:
                    time.sleep(1)
                    print("Using space")
                    ActionChains(driver).click("/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]").key_down(Keys.SPACE).key_up(Keys.SPACE)
                
                
                print(bet)
                print("Bet: %.4f Payout at: %.2f" %(bet , payouting))
                while True:    
                    payout2 = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x",""))
                    if(payout2 != lastPayout):
                        if(payouting <= payout2):
                            profit += (bet*payouting-bet)                            
                            print("Win %.6f payout %.2f" %(bet*payouting, payout2))
                            bet = betMain
                            
                        elif(payouting >  payout2):
                            profit -= bet
                            print("Lose %.6f payout %.2f" %(bet, payout2))
                            bet = bet*2
                            if(temporaryNext == "b"):                                 
                                bet = bet/4
                            if(bet >= maxBet):
                                maxBet = bet
                                print("New max bet: %.4f" %maxBet)
                        if(temporaryNext == "b"):                               
                            bet1 = bet*4
                        elif(temporaryNext == "c"):
                            bet2 = bet                               
                        elif(temporaryNext == "d"):                               
                            bet3 = bet
                        elif(temporaryNext == "e"):
                            bet4 = bet
                        elif(temporaryNext == "f"):
                            bet5 = bet
                        break
                    else:
                        time.sleep(0.3)
        print("Profit: %.6f" %profit)
        print("__________________")
        print("Bet: %.4f - %.4f - %.4f - %.4f - %.4f" %(bet1, bet2, bet3, bet4, bet5))
        print("Max bet: %.4f" %maxBet)
        timeRunSec = time.time()-timeStart
        minutes = round(timeRunSec/60)
        seconds = timeRunSec%60
        print("Time running: %d:%d" %(minutes,seconds))
        print("Bet total: %d - Bet: %d" %(timeRun, timeBet))
        print("__________________")
        if(profit <= stopLost or profit >= takeProfit):
            break
        time.sleep(1)
    else:
        time.sleep(0.3)

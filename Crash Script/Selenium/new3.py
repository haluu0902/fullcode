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
timeWin1 = 0
timeWin2 = 0
timeWin3 = 0
timeWin4 = 0
timeWin5 = 0

timeBet1 = 0
timeBet2 = 0
timeBet3 = 0
timeBet4 = 0
timeBet5 = 0

maxBet = betMain
profit = 0.00
payout2 = 0.00
timeBet = 0
timeRun = 0
temporaryNext = ""
rs1 = open("./data/history_3_8.txt", "r")
dataRs1 = rs1.read()
dataRs1 = dataRs1.split("x\n")
lenArr1 = len(dataRs1)
rs1.close()
rs = open("./data/handingResult_3_8", "r")
dataRs = rs.readline()
rs.close()
check2 = True

url = "https://bc.game/crash"
driver = webdriver.Chrome("chromedriver.exe")

def getNext(arr):
    #if(arr[4] == "a" and arr[3] == "a" and arr[2] == "a" and arr[1] == "a"):
    if(arr[3] == "a" and arr[2] == "a" and arr[1] == "a"):
        return 0
    listReturnNum = []
    valueArr=0.00
    nextNum = 0.00
    temporaryRs = ""
    stringArr = ''.join(str(e) for e in arr)
    listResult = [_.start() for _ in re.finditer(stringArr, dataRs)]
    if(len(listResult) == 0):
        return 0
    else:         
        for vrs in listResult:
            try:
                #print(dataRs1[vrs + len(stringArr)-5],dataRs1[vrs + len(stringArr)-4],dataRs1[vrs + len(stringArr)-3],dataRs1[vrs + len(stringArr)-2],dataRs1[vrs + len(stringArr)-1],dataRs1[vrs + len(stringArr)])
                temporaryRs = float(dataRs1[vrs + len(stringArr)])
                if(temporaryRs < 10):
                    listReturnNum.append(temporaryRs)                
            except:
                break
        if(len(listReturnNum) == 0):
            return 0
        return round((sum(listReturnNum)/len(listReturnNum)),2)

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
payout = 0.00
inputB = driver.find_elements_by_xpath("""//*[@class="input-control"]/input[@type="text"]""")
historyValue = [
    #handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[3]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[4]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[5]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x","")))
]
while True:
    check2=True
    try:
        check = True
        payout = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x",""))
        if(lastPayout != payout):
            del historyValue[0]
            historyValue.append(handingNumber(payout))
            payouting = getNext(historyValue)
            with open("./data/history_dice", "a+") as hd:
                hd.write("History: " + str(historyValue) + "\n")
                print("History: ", historyValue)
                hd.write("Next Bet: "+ str(payouting) + "\n")
                print("Next Bet: ", payouting)
                if(payouting > 1 and payouting <2):
                    bet = bet1
                elif(payouting >= 2 and payouting < 3):
                    bet = bet2
                elif(payouting >= 3 and payouting < 4):
                    bet = bet3
                elif(payouting >= 4 and payouting < 6):
                    bet = bet4
                elif(payouting >= 6 and payouting <= 1000):
                    bet = bet5
                elif(payouting == 0):
                    hd.write("Bet: 0 - Pass this time" + "\n")
                    print("Bet: 0 - Pass this time")
                    check= False
                lastPayout = payout
                timeRun+=1
                hd.write("Last payout: " + str(lastPayout) + "\n")
                print ("Last payout: ", lastPayout)
                if(check):
                    timeBet += 1
                    if(profit - bet <= stopLost*1.3):
                        hd.write("Stop win or lost")
                        print("Stop win or lost")
                        break
                    if(timeRun != 1):
                        ActionChains(driver).click(inputB[0]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(str(bet)).perform()
                        time.sleep(0.3)
                        ActionChains(driver).click(inputB[1]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(str(payouting)).perform()
                        time.sleep(3)
                        try:
                            betBut = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/button/div").click()
                        except:
                            hd.write("Can not Click\n")
                            print("Can not Click")
                            check2=False
                        if(check2):
                            hd.write("Bet: %.4f Payout at: %.2f\n" %(bet , payouting))
                            print("Bet: %.4f Payout at: %.2f" %(bet , payouting))
                            while True:    
                                payout2 = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x",""))
                                if(payout2 != lastPayout):
                                    if(payouting <= payout2):
                                        profit += (bet*payouting-bet)
                                        hd.write("Win %.6f payout %.2f\n" %(bet*payouting, payout2))                            
                                        print("Win %.6f payout %.2f" %(bet*payouting, payout2))
                                        bet = betMain
                                        
                                    elif(payouting >  payout2):
                                        profit -= bet
                                        hd.write("Lose %.6f payout %.2f\n" %(bet, payout2))
                                        print("Lose %.6f payout %.2f" %(bet, payout2))
                                        bet = bet*2
                                        if(payouting > 1 and payouting <=2):                                
                                            bet = bet/4
                                        if(bet >= maxBet):
                                            maxBet = bet
                                            hd.write("New max bet: %.4f\n" %maxBet)
                                            print("New max bet: %.4f" %maxBet)
                                    if(payouting > 1 and payouting <=2):
                                        if(bet == betMain):
                                            timeWin1+=1
                                        timeBet1+=1
                                        bet1 = bet*4
                                    elif(payouting > 2 and payouting <= 3):
                                        if(bet == betMain):
                                            timeWin2+=1
                                        timeBet2+=1
                                        bet2 = bet
                                    elif(payouting > 3 and payouting <= 4):
                                        if(bet == betMain):
                                            timeWin3+=1
                                        timeBet3+=1
                                        bet3 = bet
                                    elif(payouting > 4 and payouting <= 6):
                                        if(bet == betMain):
                                            timeWin4+=1
                                        timeBet4+=1
                                        bet4 = bet
                                    elif(payout > 6 and payout <= 1000):
                                        if(bet == betMain):
                                            timeWin5+=1
                                        timeBet5+=1
                                        bet5 = bet
                                    break
                                else:
                                    time.sleep(0.3)
                hd.write("Profit: %.6f\n" %profit)
                print("Profit: %.6f" %profit)
                hd.write("__________________\n")
                print("__________________")
                hd.write("Bet: %.4f - %.4f - %.4f - %.4f - %.4f\n" %(bet1, bet2, bet3, bet4, bet5))
                print("Bet: %.4f - %.4f - %.4f - %.4f - %.4f" %(bet1, bet2, bet3, bet4, bet5))
                hd.write("Time: a-%d-%d  b-%d-%d  c-%d-%d  d-%d-%d  e-%d-%d\n" %(timeWin1, timeBet1, timeWin2, timeBet2, timeWin3, timeBet3, timeWin4, timeBet4, timeWin5, timeBet5))
                print("Time: a-%d-%d  b-%d-%d  c-%d-%d  d-%d-%d  e-%d-%d" %(timeWin1, timeBet1, timeWin2, timeBet2, timeWin3, timeBet3, timeWin4, timeBet4, timeWin5, timeBet5))
                hd.write("Max bet: %.4f\n" %maxBet)
                print("Max bet: %.4f" %maxBet)
                timeRunSec = time.time()-timeStart
                minutes = round(timeRunSec/60)
                seconds = timeRunSec%60
                hd.write("Time running: %d:%d\n" %(minutes,seconds))
                print("Time running: %d:%d" %(minutes,seconds))
                hd.write("Bet total: %d - Bet: %d\n" %(timeRun, timeBet))
                print("Bet total: %d - Bet: %d" %(timeRun, timeBet))
                hd.write("__________________\n\n")
                print("__________________\n")
            if(profit <= stopLost or profit >= takeProfit):
                hd.write("Stop win or lost")
                break
        else:
            time.sleep(0.3)
    except:
        hd.write("Stop breaking")
        break

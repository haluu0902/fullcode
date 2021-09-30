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
bet6 = betMain
bet7 = betMain
bet8 = betMain
bet9 = betMain
bet10 = betMain
maxBet = betMain
profit = 0.00
payout2 = 0.00
timeBet = 0
timeRun = 0
temporaryNext = ""
rs1 = open("./data/history_18_7.txt", "r")
dataRs1 = rs1.read()
dataRs1 = dataRs1.split("x\n")
lenArr1 = len(dataRs1)
rs1.close()
rs = open("./data/handingResult_18_7", "r")
dataRs = rs.readline()
rs.close()
url = "https://bc.game/crash"
driver = webdriver.Chrome("chromedriver.exe")

def getNext(arr):
    if(arr[4] == "a" and arr[3] == "a" and arr[2] == "a" and arr[1] == "a"):
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
        temporaryRs= random.choice(listReturnNum)
        if(temporaryRs > 10):
            temporaryRs = 10
        return temporaryRs

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
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[3]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[4]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[5]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x","")))
]
while True:
    check = True
    payout = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x",""))
    if(lastPayout != payout):
        del historyValue[0]
        historyValue.append(handingNumber(payout))
        payouting = getNext(historyValue)
        print("History: ", historyValue)
        print("Next Bet: ", payouting)
        if(payouting > 1 and payouting <2):
            bet = bet1
        elif(payouting >= 2 and payouting < 3):
            bet = bet2
        elif(payouting >= 3 and payouting < 4):
            bet = bet3
        elif(payouting >= 4 and payouting < 5):
            bet = bet4
        elif(payouting >= 5 and payouting < 6):
            bet = bet5
        elif(payouting >= 6 and payouting < 7):
            bet = bet6
        elif(payouting >= 7 and payouting < 8):
            bet = bet7
        elif(payouting >= 8 and payouting < 9):
            bet = bet8
        elif(payouting >= 9 and payouting < 10):
            bet = bet9
        elif(payouting >= 10 and payouting < 11):
            bet = bet10
        elif(payouting == 0):
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
                time.sleep(1)
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
                            if(payouting > 1 and payouting <=2):                                 
                                bet = bet/4
                            if(bet >= maxBet):
                                maxBet = bet
                                print("New max bet: %.4f" %maxBet)
                        if(payouting > 1 and payouting <=2):
                            bet1 = bet*4
                        elif(payouting >= 2 and payouting < 3):
                            bet2 = bet
                        elif(payouting >= 3 and payouting < 4):
                            bet3 = bet
                        elif(payouting >= 4 and payouting < 5):
                            bet4 = bet
                        elif(payouting >= 5 and payouting < 6):
                            bet5 = bet
                        elif(payouting >= 6 and payouting < 7):
                            bet6 = bet
                        elif(payouting >= 7 and payouting < 8):
                            bet7 = bet
                        elif(payouting >= 8 and payouting < 9):
                            bet8 = bet
                        elif(payouting >= 9 and payouting < 10):
                            bet9 = bet
                        elif(payouting >= 10 and payouting < 11):
                            bet10 = bet
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
    else:
        time.sleep(0.3)

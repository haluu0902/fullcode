import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
import time
import math

urlC = "https://bc.game/crash"
urlT = "https://bc.game/crash/trenball"
ra = open("./data/rs.txt", "r")
dataRa = ra.read().split("\n")
ra.close()
driver = webdriver.Chrome("chromedriver.exe")
driver.get(urlC)
crash = driver.window_handles[0]
a = input("Continue: ")
driver.execute_script("window.open('');")
trendball = driver.window_handles[1]
driver.switch_to_window(trendball)
driver.get(urlT)
time.sleep(3)
driver.switch_to_window(crash)

timeRun = 0
timeBet = 0
lastPayout = 0
payout = 0
profit = 0
betMain = round(float(input("Bet: ")),4)
payouting = round(float(input("Payout: ")),2)
stopLost = round(float(input("Stop lost: ")),4)*(-1)
takeProfit = round(float(input("Take profit: ")),4)
print("Success bet: ", betMain)
bet = betMain
arrBet = [bet,bet,bet,bet,bet,bet,bet]
noBet = 0
check2 = True
lostPr = 0
winP = 0
maxBet = bet
timeStart = time.time()


inputB = driver.find_elements_by_xpath("""//*[@class="input-control"]/input[@type="text"]""")
driver.switch_to_window(trendball)
inputC = driver.find_elements_by_xpath("""//*[@class="input-control"]/input[@type="text"]""")
driver.switch_to_window(crash)

def handingNumber(value):
    if(value >= 1 and value < 2):
        return 0
    elif(value >= 2 and value < 10):
        return 1
    else:
        return 2

def getnext(arr):
    stringArr = ','.join(str(e) for e in arr)
    for dt in dataRa:
        if(dt == stringArr[(len(stringArr) - len(dt)):]):
            return True
    return False
historyValue = [
    #handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[0]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[2]").get_attribute('textContent').replace("x",""))),
    handingNumber(float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[2]").get_attribute('textContent').replace("x",""))),
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
            timeRun+=1
            if(len(historyValue) == 7):
                del historyValue[0]
            historyValue.append(handingNumber(payout))
            lastPayout = payout
            with open("./data/history_dice", "a+") as hd:
                hd.write("History: " + str(historyValue) + "\n")
                print("History: ", historyValue)
                hd.write("Array Bet: " + str(arrBet) + "\n")
                print("Array Bet: ", arrBet)
                if(getnext(historyValue)):
                    noBet = randint(0, 4)
                    bet = arrBet[noBet]                    
                    hd.write("Last payout: " + str(lastPayout) + "\n")
                    print ("Last payout: ", lastPayout)
                    timeBet += 1
                    if(profit - bet <= stopLost*1.3):
                        hd.write("Stop win or lost")
                        print("Stop win or lost")
                        break
                    if(timeRun != 1):
                        ActionChains(driver).click(inputB[0]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(str(bet)).perform()
                        time.sleep(0.3)
                        ActionChains(driver).click(inputB[1]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(str(payouting)).perform()
                        driver.switch_to_window(trendball)
                        time.sleep(0.3)
                        ActionChains(driver).click(inputC[0]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(str(bet/2)).perform()
                        time.sleep(3)
                        try:
                            betBut = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/button/div").click()
                            driver.switch_to_window(crash)
                            betBut = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/button/div").click()
                            
                            
                        except:
                            hd.write("Can not Click\n")
                            print("Can not Click")
                            check2=False
                            try:
                                driver.switch_to_window(crash)
                            except:
                                pass
                        if(check2):
                            hd.write("Bet: %.4f Payout at: %.2f\n" %(bet , payouting))
                            print("Bet: %.4f Payout at: %.2f" %(bet , payouting))
                            while True:    
                                payout2 = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x",""))
                                if(payout2 != lastPayout):
                                    if(payouting <= payout2 and payout2 < 2):
                                        winP = ((bet*(payouting-1)) + bet/2*0.96)
                                        profit += winP
                                        hd.write("Win %.6f payout %.2f\n" %(winP, payout2))                            
                                        print("Win %.6f payout %.2f" %(winP, payout2))
                                        bet = betMain 
                                    else:
                                        if(payouting > payout2):
                                            lostPr = bet - bet/2*0.96
                                        elif(payout2 >= 2):
                                            lostPr = bet/2 - bet*(payouting-1)
                                        profit -= lostPr
                                        hd.write("Lose %.6f - Payout %.2f\n" %(lostPr, payout2))
                                        print("Lose %.6f - Payout %.2f" %(lostPr, payout2))
                                        bet = bet*2 
                                        if(bet >= maxBet):
                                            maxBet = bet
                                            hd.write("New max bet: %.4f\n" %maxBet)
                                            print("New max bet: %.4f" %maxBet)
                                    arrBet[noBet] = bet
                                    break
                                else:
                                    time.sleep(0.3)
                    hd.write("Profit: %.6f\n" %profit)
                    print("Profit: %.6f" %profit)
                    hd.write("__________________\n")
                    print("__________________")
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
                    hd.write("Bet: 0 - Pass this time" + "\n")
                    print("Bet: 0 - Pass this time")
            
        else:
            time.sleep(0.3)
    except:
        with open("./data/history_dice", "a+") as hd:
            hd.write("Stop breaking")
            hd.write("__________________\n\n")                    
        print("Stop breaking")
        print("__________________\n")
        break
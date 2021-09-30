import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import time
import math
import re
import operator

url = "https://bc.game/hash-dice"
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
time.sleep(3)


a = input("Continue: ")
bet = float(input("Bet: "))
yourPayout = float(input("Payout: "))
takeProfit = float(input("Take profit: "))
stopLost = float(input("Stop lost: "))
highOrLow = int(input("High or low (type 1 for high and -1 for low): "))
lastPayout=0
payout = 0
betMain = bet
betArr = [bet, bet, bet, bet, bet]
timeRun = 0
noBet = 0
timeBet = 0
profit =0
timeWin = 0
timeLost = 0
chance = 0
inputB = driver.find_elements_by_xpath("""//*[@class="input-control"]/input[@type="text"]""")
for i in range(10, 0, -1):
    try:
        driver.find_element_by_xpath("/html/body/div["+ str(i)+"]/div/div[1]/button").click()
        tabButton = driver.find_element_by_xpath("/html/body/div["+ str(i)+"]/div/div[1]/button")
        break
    except:
        pass
    
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[3]/button[3]").click()

if(highOrLow == 1):
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/span/span[1]").click() 
else:
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/span/span[3]").click()
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
a = input("Continue: ")
time.sleep(3)
while True:
    check2=True
    check = True
    try:
        chance = (float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/span/span[2]").get_attribute('textContent').replace(">","")))
    except:
        chance = (float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/span/span[2]").get_attribute('textContent').replace("<","")))
    payout = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/div").get_attribute('textContent'))
    if(lastPayout != payout):
        timeRun+=1
        lastPayout = payout
        print("Array Bet: " + str(betArr))
        print("Last payout: " + str(lastPayout))
        noBet = randint(0, 4)
        bet = betArr[noBet]
        timeBet += 1
        if(profit - bet <= stopLost*(-1.3)):
            print("Stop win or lost")
            break
        while True:
            try:
                inputB = driver.find_elements_by_xpath("""//*[@class="input-control"]/input[@type="text"]""")
                ActionChains(driver).click(inputB[0]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(("%.8f" %(bet))).perform()
                time.sleep(0.1)
                ActionChains(driver).click(inputB[1]).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(str(yourPayout)).perform()
                time.sleep(0.1)
                break
            except:
                pass
        try:
            betBut = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div/button/div").click() 
        except:
            print("Can not Click")
            check2=False
        if(check2):
            print(str(timeRun) + ".Beting: " + str(bet))
            while True:    
                payout2 = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/div").get_attribute('textContent'))
                if(payout2 != lastPayout):
                    if(chance*highOrLow < payout2*highOrLow):
                        winP = bet*(yourPayout-1)
                        profit += winP
                        print("Win: " + str(round(winP,4)))
                        print("Payout: " + str(payout2))
                        if(bet + winP < betMain * 2):
                            bet = bet+winP
                        else:
                            bet = betMain
                        timeWin +=1
                        print("Time win: " + str(timeWin)) 
                    else:
                        timeLost+=1
                        lostPr = bet
                        profit -= lostPr
                        print("Lose: " + str(round(lostPr,4)))
                        print("Payout: " + str(payout2))
                        bet = bet * (1 + 1/(yourPayout-1))
                        print("Time lost: " + str(timeLost))
                        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                        if(highOrLow == -1):
                            highOrLow = 1
                            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/span/span[1]").click() 
                        else:
                            highOrLow = -1
                            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[3]/span/span[3]").click()
                    betArr[noBet] = bet
                    break
        print("Profit: " + str(round(profit,4)))
        if(profit <= stopLost*(-1) or profit >= takeProfit):
            print("Stop win or lost")
            break
        if(timeRun%20 == 0):
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[3]/button[6]").click()
            time.sleep(0.1)
            check3 = True
            while check3:
                for i in range(50, 0, -1):
                    try:
                        driver.find_element_by_xpath("/html/body/div[" + str(i) + "]/div/div[2]/div/div[5]/button/div").click()
                        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                        check3 = False
                        break
                    except:
                        pass
    
        
            
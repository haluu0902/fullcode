import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
import time
import math

timeStart = time.time()
timeRunSec = 0
minutes =0
seconds =0

lastPayout=0
payouting = 2
betMain = round(float(input("Bet: ")),2)
print("Success bet: ", betMain)
bet = betMain
bet1 = betMain*4
bet2 = betMain
bet3 = betMain
maxBet = betMain
profit = 0.00
payout2 = 0.00
timeBet = 0
timeRun = 0
url = "https://bc.game/crash"

driver = webdriver.Chrome("chromedriver.exe")

driver.get(url)
time.sleep(3)
a = input("Continue: ")
payout = 0.00
inputB = driver.find_elements_by_xpath("""//*[@class="input-control"]/input[@type="text"]""")
while True:
    check = True
    payout = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x",""))
    if(lastPayout != payout):
        if(payout > 2 and payout <=3):
            payouting = round((payout - math.floor(payout)+1),2)
            bet = bet1
        elif(payout > 3 and payout <= 7):
            payouting = round((payout - math.floor(payout)+2),2)
            bet = bet2
        elif(payout > 7 and payout <= 10):
            payouting = round((payout - math.floor(payout)+3),2)
            bet = bet3
        else:
            print("Pass")
            check= False
        lastPayout = payout
        timeRun+=1
        print (lastPayout)
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
                            print("Win %.4f payout %.2f" %(bet*payouting, payout2))
                            bet = betMain
                            
                        elif(payouting >  payout2):
                            profit -= bet
                            print("Lose %.4f payout %.2f" %(bet, payout2))
                            bet = bet*2
                            if(payouting > 1 and payouting < 2):                                 
                                bet = bet/4
                            if(bet >= maxBet):
                                maxBet = bet
                                print("New max bet: %.4f" %maxBet)
                        if(payouting > 1 and payouting < 2):                               
                            bet1 = bet*4
                        elif(payouting >= 2 and payouting < 3):
                            bet2 = bet                               
                        elif(payouting >= 3 and payouting < 4):                               
                            bet3 = bet
                        break
                    else:
                        time.sleep(0.3)
        print("Profit: %.4f" %profit)
        print("__________________")
        print(bet1)
        print(bet2)
        print(bet3)
        timeRunSec = time.time()-timeStart
        minnutes = round(timeRunSec/60)
        seconds = timeRunSec%60
        print("Time running: %d:%d" %(minutes,seconds))
        print("Bet total: %d - Bet: %d" %(timeRun, timeBet))
        print("__________________")
        time.sleep(1)
    else:
        time.sleep(0.3)

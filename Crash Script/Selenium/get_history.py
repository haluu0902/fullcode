import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

payout = 0.00
payouting = 0.00
url = "https://bc.game/crash"

driver = webdriver.Chrome("chromedriver.exe")

driver.get(url)
time.sleep(3)


a = input("Continue: ")

while True:    
    payouting = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x","")
    if(payout != payouting):
        payout = payouting
        f = open("./data/history_1.txt", "a+")
        f.write(payout)
        f.write("-")
        f.close()
        print (payout)
    else:
        time.sleep(0.3)
import selenium
from selenium import webdriver
from threading import Thread

class ControllChrome:
    def __init__(self, numberOfBrowser):
        self.numberOfBrowser = numberOfBrowser
        self.driver = []
        self.url = "https://bc.game/promotion"
        self.options = webdriver.ChromeOptions()        
    def open_browser(self):
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        for i in range(self.numberOfBrowser):
            mid = webdriver.Chrome("chromedriver.exe", options=self.options)
            self.driver.append(mid)
    def send_code(self,code):
        for i in range(self.numberOfBrowser):
            self.driver[i].find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div/input").send_keys(code)
            self.driver[i].find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/button/div").click()
            

import tkinter as tk
from tkinter import *

import time
from random import randint
import threading

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
import time
import math

import discord
import asyncio
from threading import Thread
from sendMess import send

def auto_run():
    root = tk.Tk()
    root.title("Auto Crash BC.Game - By: SaviorXXI")
    img = tk.Image("photo", file="./images/icon.png")
    root.iconbitmap(r'./images/icon.ico')
    root.resizable(0,0)
    root.tk.call('wm','iconphoto', root._w, img)

    frame1 = Frame(root, relief=RAISED, borderwidth=1)
    frame1.pack(fill=X, padx=0, pady=0)

    bet_label = Label(frame1, text="Bet:", width=12)
    bet_label.pack(side=LEFT, padx=0, pady=0)
    value_bet = StringVar(root, value='10')
    input_bet = Entry(frame1,textvariable=value_bet)
    input_bet.pack(side=LEFT, padx=5, pady=0)

    payout_label = Label(frame1, text="Payout:", width=12)
    payout_label.pack(side=LEFT, padx=0, pady=0)
    value_payout = StringVar(root, value='1.2')
    input_payout = Entry(frame1,textvariable=value_payout)
    input_payout.pack(side=LEFT, padx=5, pady=0)

    frame2 = Frame(root, relief=RAISED, borderwidth=1)
    frame2.pack(fill=X, padx=0, pady=0)

    tp_label = Label(frame2, text="Take Profit:", width=12)
    tp_label.pack(side=LEFT, padx=0, pady=0)
    value_tp = StringVar(root, value='1000')
    input_tp = Entry(frame2,textvariable=value_tp)
    input_tp.pack(side=LEFT, padx=2, pady=0)

    sl_label = Label(frame2, text="Stop Lost:", width=12)
    sl_label.pack(side=LEFT, padx=0, pady=0)
    value_sl = StringVar(root, value='1000')
    input_sl = Entry(frame2,textvariable=value_sl)
    input_sl.pack(side=LEFT, padx=2, pady=0)

    frame_notification_1 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_1.pack(fill=X, padx=0, pady=0)

    history_label = Label(frame_notification_1, text="History: [0, 0, 0, 0, 0, 0, 0]", width=20)
    history_label.pack(side=LEFT, padx=0, pady=0)

    array_bet_label = Label(frame_notification_1, text="Array Bet: [0, 0, 0, 0, 0]", width=50)
    array_bet_label.pack(side=LEFT, padx=0, pady=0)

    frame_notification_2 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_2.pack(fill=X, padx=0, pady=0)

    last_payout_label = Label(frame_notification_2, text="Last payout: 0", width=20)
    last_payout_label.pack(side=LEFT, padx=0, pady=0)

    beting_label = Label(frame_notification_2, text="Beting: 0", width=20)
    beting_label.pack(side=LEFT, padx=0, pady=0)

    bet_max_label = Label(frame_notification_2, text="Bet max: 0", width=20)
    bet_max_label.pack(side=LEFT, padx=0, pady=0)

    frame_notification_3 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_3.pack(fill=X, padx=0, pady=0)

    time_label = Label(frame_notification_3, text="Time running: 0 min", width=20)
    time_label.pack(side=LEFT, padx=0, pady=0)

    time_run_label = Label(frame_notification_3, text="Time run: 0", width=20)
    time_run_label.pack(side=LEFT, padx=0, pady=0)

    time_bet_label = Label(frame_notification_3, text="Time bet: 0", width=20)
    time_bet_label.pack(side=LEFT, padx=0, pady=0)


    frame_notification_4 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_4.pack(fill=X, padx=0, pady=0)

    time_win_label = Label(frame_notification_4, text="Time win: 0", width=20, fg = "green")
    time_win_label.pack(side=LEFT, padx=0, pady=0)

    time_lost_label = Label(frame_notification_4, text="Time lost: 0", width=20, fg = "red")
    time_lost_label.pack(side=LEFT, padx=0, pady=0)

    profit_label = Label(frame_notification_4, text="Profit: 0", width=25, fg = "green")
    profit_label.pack(side=LEFT, padx=0, pady=0)


    frame_notification_5 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_5.pack(fill=X, padx=0, pady=0)

    textarea = Text(frame_notification_5, width = 70,height=10)
    textarea.pack(side=LEFT, padx=10, pady=10)
    textarea.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    textarea.tag_config('lost', foreground="red")
    textarea.tag_config('win', foreground="green")

    scrollbar = Scrollbar(frame_notification_5, command=textarea.yview)
    scrollbar.grid(row=0, column=1, sticky='nsew')
    textarea['yscrollcommand'] = scrollbar.set




    frame_final = Frame(root, relief=RAISED, borderwidth=1)
    frame_final.pack(fill=X, padx=0, pady=0)
    status_label = Label(frame_final, text="Status: relax", width=15, fg = "blue")
    status_label.pack(side=LEFT, padx=0, pady=0)
    send_message_label = Label(frame_final, text="Send message: off", width=15, fg = "red")
    send_message_label.pack(side=LEFT, padx=0, pady=0)

    def login():
        global driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome("chromedriver.exe", options=options)
        driver.get("https://bc.game/crash")

    def rule():
        try:
            
            status_label.config(fg ="green")
            status_label["text"] = "Status: runing"
            urlC = "https://bc.game/crash"
            urlT = "https://bc.game/crash/trenball"
            ra = open("./data/rs.txt", "r")
            dataRa = ra.read().split("\n")
            ra.close()
            crash = driver.window_handles[0]
            try:
                trendball = driver.window_handles[1]
            except:
                driver.execute_script("window.open('');")
                trendball = driver.window_handles[1]
                pass            
            driver.switch_to_window(trendball)
            driver.get(urlT)
            time.sleep(3)
            driver.switch_to_window(crash)

            timeRun = 0
            timeBet = 0
            timeWin = 0
            timeLost = 0
            lastPayout = 0
            payout = 0
            profit = 0
            betMain = float(input_bet.get())
            payouting = float(input_payout.get())
            stopLost = float(input_sl.get())*(-1)
            takeProfit = float(input_tp.get())
            print("Success bet: ", betMain)
            bet = betMain
            arrBet = [bet,bet,bet,bet,bet]
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
                        with open("./data/history_dice.txt", "a+") as hd:
                            hd.write("History: " + str(historyValue) + "\n")
                            history_label["text"] = ("History: " + str(historyValue))
                            hd.write("Array Bet: " + str(arrBet) + "\n")
                            array_bet_label["text"] = "Array Bet: " + str(arrBet)
                            hd.write("Last payout: " + str(lastPayout) + "\n")
                            last_payout_label["text"] = "Last payout: " + str(lastPayout)
                            if(getnext(historyValue)):
                                noBet = randint(0, 4)
                                bet = arrBet[noBet]
                                timeBet += 1
                                if(profit - bet <= stopLost*1.3):
                                    hd.write("Stop win or lost")
                                    textarea.insert(END,"Stop win or lost"+"\n")
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
                                        textarea.insert(END,"Can not Click"+"\n","lost")
                                        try:
                                            driver.switch_to_window(crash)
                                        except:
                                            pass
                                        check2=False
                                    if(check2):
                                        hd.write("Bet: %.4f Payout at: %.2f\n" %(bet , payouting))
                                        beting_label["text"] = "Beting: " + str(bet)
                                        textarea.insert(END,str(timeRun) + ".Beting: " + str(bet) +"\n")
                                        while True:    
                                            payout2 = float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[6]/div[2]").get_attribute('textContent').replace("x",""))
                                            if(payout2 != lastPayout):
                                                if(payouting <= payout2 and payout2 < 2):
                                                    winP = ((bet*(payouting-1)) + bet/2*0.96)
                                                    profit += winP
                                                    hd.write("Win %.6f payout %.2f\n" %(winP, payout2))
                                                    textarea.insert(END,"Win: " + str(round(winP,4)) +"\n", "win")
                                                    textarea.insert(END,"Payout: " + str(payout2) +"\n")
                                                    bet = betMain
                                                    timeWin +=1
                                                    time_win_label["text"] = "Time win: " + str(timeWin) 
                                                else:
                                                    if(payouting > payout2):
                                                        lostPr = bet - bet/2*0.96
                                                    elif(payout2 >= 2):
                                                        lostPr = bet/2 - bet*(payouting-1)
                                                    profit -= lostPr
                                                    hd.write("Lose %.6f - Payout %.2f\n" %(lostPr, payout2))
                                                    textarea.insert(END,"Lose: " + str(round(lostPr,4)) +"\n", "lost")
                                                    textarea.insert(END,"Payout: " + str(payout2) +"\n")
                                                    bet = bet*2 
                                                    if(bet >= maxBet):
                                                        maxBet = bet
                                                        hd.write("New max bet: %.4f\n" %maxBet)
                                                        textarea.insert(END,"New max bet: " + str(maxBet) +"\n","lost")
                                                        bet_max_label["text"] = "New max bet: " + str(maxBet)
                                                    timeLost +=1
                                                    time_lost_label["text"] = "Time lost: " + str(timeLost) 
                                                arrBet[noBet] = bet
                                                break
                                            else:
                                                time.sleep(0.3)
                                hd.write("Profit: %.6f\n" %profit)
                                if(profit > 0):
                                    profit_label.config(fg="green")                            
                                else:
                                    profit_label.config(fg="red")   
                                profit_label["text"] = "Profit: " + str(round(profit,4))
                                hd.write("__________________\n")                    
                                timeRunSec = time.time()-timeStart
                                minutes = round(timeRunSec/60)
                                seconds = timeRunSec%60
                                hd.write("Time running: %d:%d\n" %(minutes,seconds))
                                time_label["text"] = "Time running: " + str(minutes)
                                hd.write("Bet total: %d - Bet: %d\n" %(timeRun, timeBet))                    
                                time_bet_label["text"] = "Time bet: " + str(timeBet)
                                hd.write("__________________\n\n")
                                if(profit <= stopLost or profit >= takeProfit):
                                    hd.write("Stop win or lost")
                                    textarea.insert(END,"Stop win or lost" +"\n","lost")
                                    break
                            else:
                                hd.write("Bet: 0 - Pass this time" + "\n")
                                beting_label["text"] = "Bet: 0"
                                textarea.insert(END,str(timeRun) + ".Bet: 0 - Pass this time" +"\n")
                            time_run_label["text"] = "Time running: " + str(timeRun)
                            textarea.insert(END,"__________________" +"\n","lost")
                    else:
                        time.sleep(0.3)
                except Exception as e:
                    with open("./data/history_dice.txt", "a+") as hd:
                        hd.write("Stop breaking")
                        hd.write("__________________\n\n")                    
                    textarea.insert(END,"Stop breaking!" +"\n","lost")
                    textarea.insert(END,e ,"lost")
                    textarea.insert("\n","lost")
                    textarea.insert(END,"__________________" +"\n","lost")
                    textarea.insert(END,"__________________" +"\n","lost")
                    status_label.config(fg = "red")
                    status_label["text"] = "Status: break"
                    break
        except Exception as e:
            status_label.config(fg = "red")
            textarea.insert(END,e ,"lost")
            textarea.insert("\n","lost")
            textarea.insert(END,"__________________" +"\n","lost")
            status_label["text"] = "Status: fail"
    def send_message():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_until_complete(send())
        loop.close()


    def run():
        t = threading.Thread(target=rule).start()

    def run_send_message():
        send_message_label.config(fg ="green")
        send_message_label["text"] = "Send message: on"
        t1 = threading.Thread(target=send_message).start()

    login_button = Button(frame1, text="Login", command=login)
    login_button.pack(side=RIGHT, padx=5, pady=0) 
    start_button = Button(frame_final, text="Start Bet", command=run)
    start_button.pack(side=RIGHT, padx=5, pady=5) 
    send_message_button = Button(frame_final, text="Send Message to Discord", command=run_send_message)
    send_message_button.pack(side=RIGHT, padx=5, pady=5) 
    root.mainloop()
import tkinter as tk
from tkinter import *
from tkinter import font

import time
from random import randint
import threading
import traceback


import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
import time
import math
from PIL import Image, ImageTk

import discord
import asyncio
from threading import Thread


def auto_run():
    root = tk.Tk()
    root.title("Auto Crash Trendball BC.Game - By: SaviorXXI")
    img = tk.Image("photo", file="./images/icon.png")
    root.iconbitmap(r'./images/icon.ico')
    root.resizable(0, 0)
    root.tk.call('wm', 'iconphoto', root._w, img)

    frame1 = Frame(root, relief=RAISED, borderwidth=1)
    frame1.pack(fill=X, padx=0, pady=0)

    bet_label = Label(frame1, text="Bet:", anchor='w', width=10)
    bet_label.pack(side=LEFT, padx=10, pady=0)
    value_bet = StringVar(root, value='10')
    input_bet = Entry(frame1, width=10, textvariable=value_bet)
    input_bet.pack(side=LEFT, padx=2, pady=0)

    value_checkbox_bet_by_balace = IntVar(value = 1)
    checkbox_bet_by_balace = Checkbutton(
        frame1, text='Bet by multiply balance', variable=value_checkbox_bet_by_balace)
    checkbox_bet_by_balace.pack(side=LEFT, padx=20, pady=0)

    value_input_multiple_balance = StringVar(root, value='2700')
    input_multiple_balance = Entry(
        frame1, width=9, textvariable=value_input_multiple_balance)
    input_multiple_balance.pack(side=LEFT, padx=0, pady=0)

    frame2 = Frame(root, relief=RAISED, borderwidth=1)
    frame2.pack(fill=X, padx=0, pady=0)

    tp_label = Label(frame2, text="Take Profit:", anchor='w', width=10)
    tp_label.pack(side=LEFT, padx=10, pady=0)
    value_tp = StringVar(root, value='1000')
    input_tp = Entry(frame2, width=10, textvariable=value_tp)
    input_tp.pack(side=LEFT, padx=0, pady=0)

    sl_label = Label(frame2, text="Stop Lost:", anchor='w', width=12)
    sl_label.pack(side=LEFT, padx=20, pady=0)
    value_sl = StringVar(root, value='1000')
    input_sl = Entry(frame2, textvariable=value_sl)
    input_sl.pack(side=LEFT, padx=0, pady=0)

    frame_notification_1 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_1.pack(fill=X, padx=0, pady=0)

    history_title = Label(
        frame_notification_1, text="History: ", anchor='w', width=10)
    history_title.pack(side=LEFT, padx=10, pady=0)

    history_1 = Label(frame_notification_1, anchor='w')
    history_1.pack(side=LEFT, padx=0, pady=0)
    history_2 = Label(frame_notification_1, anchor='w')
    history_2.pack(side=LEFT, padx=0, pady=0)
    history_3 = Label(frame_notification_1, anchor='w')
    history_3.pack(side=LEFT, padx=0, pady=0)
    history_4 = Label(frame_notification_1, anchor='w')
    history_4.pack(side=LEFT, padx=0, pady=0)
    history_5 = Label(frame_notification_1, anchor='w')
    history_5.pack(side=LEFT, padx=0, pady=0)
    history_6 = Label(frame_notification_1, anchor='w')
    history_6.pack(side=LEFT, padx=0, pady=0)
    history_7 = Label(frame_notification_1, anchor='w')
    history_7.pack(side=LEFT, padx=0, pady=0)

    history_label = [history_1, history_2, history_3,
                     history_4, history_5, history_6, history_7]

    frame_notification_2 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_2.pack(fill=X, padx=0, pady=0)

    last_payout_label_title = Label(frame_notification_2,
                              text="Last payout: ", anchor='w', width=10)
    last_payout_label_title.pack(fill=X, side=LEFT, padx=10, pady=0)

    last_payout_label = Label(frame_notification_2,
                              text="0.0", anchor='w', width=10)
    last_payout_label.pack(fill=X, side=LEFT, padx=0, pady=0)

    frame_notification_2_1 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_2_1.pack(fill=X, padx=0, pady=0)

    beting_label_title = Label(frame_notification_2_1,
                         text="Bet: ", anchor='w', width=10)
    beting_label_title.pack(side=LEFT, padx=10, pady=0)

    beting_label = Label(frame_notification_2_1,
                         text="0.00000000", anchor='w', width=20)
    beting_label.pack(side=LEFT, padx=0, pady=0)

    image_label_title = Label(frame_notification_2_1,
                              anchor='w', text="Bet color:", width=10)
    image_label_title.pack(side=LEFT, padx=0, pady=0)

    image_label = Label(frame_notification_2_1, anchor='w')
    image_label.pack(side=LEFT, padx=0, pady=0)

    frame_notification_2_2 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_2_2.pack(fill=X, padx=0, pady=0)

    bet_max_label_title = Label(
        frame_notification_2_2, text="Biggest bet: ", anchor='w', width=10)
    bet_max_label_title.pack(side=LEFT, padx=10, pady=0)

    bet_max_label = Label(
        frame_notification_2_2, text="0.00000000", anchor='w', width=20)
    bet_max_label.pack(side=LEFT, padx=0, pady=0)

    with_prediction_label_title = Label(
        frame_notification_2_2, text="From: ", anchor='w', width=10)
    with_prediction_label_title.pack(side=LEFT, padx=0, pady=0)

    with_prediction_label = Label(
        frame_notification_2_2, text="GGGGGGG-G", anchor='w', width=10)
    with_prediction_label.pack(side=LEFT, padx=0, pady=0)

    frame_notification_3 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_3.pack(fill=X, padx=0, pady=0)

    time_run_label_title = Label(frame_notification_3,
                           text="Time run: ", anchor='w', width=10)
    time_run_label_title.pack(side=LEFT, padx=10, pady=0)

    time_run_label = Label(frame_notification_3,
                           text="0", anchor='w', width=20)
    time_run_label.pack(side=LEFT, padx=0, pady=0)

    time_bet_label_title = Label(frame_notification_3,
                           text="Time bet: ", anchor='w', width=10)
    time_bet_label_title.pack(side=LEFT, padx=0, pady=0)

    time_bet_label = Label(frame_notification_3,
                           text="0", anchor='w', width=10)
    time_bet_label.pack(side=LEFT, padx=0, pady=0)

    frame_notification_4 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_4.pack(fill=X, padx=0, pady=0)

    time_win_label_title = Label(
        frame_notification_4, text="Time win: ", anchor='w', width=10, fg="green")
    time_win_label_title.pack(side=LEFT, padx=10, pady=0)

    time_win_label = Label(
        frame_notification_4, text="0", anchor='w', width=20, fg="green")
    time_win_label.pack(side=LEFT, padx=0, pady=0)

    time_lost_label_title = Label(
        frame_notification_4, text="Time lost: ", anchor='w', width=10, fg="red")
    time_lost_label_title.pack(side=LEFT, padx=0, pady=0)

    time_lost_label = Label(
        frame_notification_4, text="0", anchor='w', width=10, fg="red")
    time_lost_label.pack(side=LEFT, padx=0, pady=0)

    frame_notification_4_1 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_4_1.pack(fill=X, padx=0, pady=0)

    profit_label_title = Label(
        frame_notification_4_1, text="Profit: ", anchor='w', width=10, fg="green")
    profit_label_title.pack(side=LEFT, padx=10, pady=0)

    profit_label = Label(
        frame_notification_4_1, text="0.00000000", anchor='w', width=20, fg="green")
    profit_label.pack(side=LEFT, padx=0, pady=0)

    time_label_title = Label(frame_notification_4_1,
                       text="Time running: ", anchor='w', width=10)
    time_label_title.pack(side=LEFT, padx=00, pady=0)

    time_label = Label(frame_notification_4_1,
                       text="0:0", anchor='w', width=10)
    time_label.pack(side=LEFT, padx=0, pady=0)

    frame1_1 = Frame(root, relief=RAISED, borderwidth=1)
    frame1_1.pack(fill=X, padx=0, pady=0)

    value_checkbox_cal_every_min = IntVar(value=1)
    checkbox_cal_every_min = Checkbutton(
        frame1_1, text='Calculate bet by balance again every', variable=value_checkbox_cal_every_min)
    checkbox_cal_every_min.pack(side=LEFT, padx=10, pady=0)

    value_input_min_cal = StringVar(root, value='60')
    input_min_cal = Entry(frame1_1, width=5, textvariable=value_input_min_cal)
    input_min_cal.pack(side=LEFT, padx=0, pady=0)

    minutes_label = Label(frame1_1, text="minutes")
    minutes_label.pack(side=LEFT, padx=0, pady=0)

    frame1_1_1 = Frame(root, relief=RAISED, borderwidth=1)
    frame1_1_1.pack(fill=X, padx=0, pady=0)

    value_checkbox_pause = IntVar(value=1)
    checkbox_pause= Checkbutton(
        frame1_1_1, text='Pause to next hour when get', variable=value_checkbox_pause)
    checkbox_pause.pack(side=LEFT, padx=10, pady=0)

    value_input_percent = StringVar(root, value='10')
    input_percent = Entry(frame1_1_1, width=5, textvariable=value_input_percent)
    input_percent.pack(side=LEFT, padx=0, pady=0)

    percent_label = Label(frame1_1_1, text="percent balance")
    percent_label.pack(side=LEFT, padx=0, pady=0)

    frame_guess_setting_1 = Frame(root, relief=RAISED, borderwidth=1)
    frame_guess_setting_1.pack(fill=X, padx=0, pady=0)

    value_checkbox_replace = IntVar(value=1)
    checkbox_replace = Checkbutton(
        frame_guess_setting_1, text='Replace Y = G when results do not match', variable=value_checkbox_replace)
    checkbox_replace.pack(side=LEFT, padx=10, pady=0)

    frame_guess_setting_2 = Frame(root, relief=RAISED, borderwidth=1)
    frame_guess_setting_2.pack(fill=X, padx=0, pady=0)

    value_checkbox_separate_prediction_money = IntVar(value=0)
    checkbox_separate_prediction_money = Checkbutton(
        frame_guess_setting_2, text='Separation of prediction and money', variable=value_checkbox_separate_prediction_money)
    checkbox_separate_prediction_money.pack(side=LEFT, padx=10, pady=0)

    frame_guess = Frame(root, relief=RAISED, borderwidth=1)
    frame_guess.pack(fill=X, padx=0, pady=0)
    textarea_guess = Text(frame_guess, width=57, height=5)
    textarea_guess.pack(side=LEFT, padx=10, pady=10)
    textarea_guess.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    textarea_guess.tag_config('lost', foreground="red")
    textarea_guess.tag_config('win', foreground="green")
    bold_font = font.Font(textarea_guess, textarea_guess.cget("font"))
    bold_font.configure(weight="bold")
    textarea_guess.tag_configure("run", font=bold_font, foreground="blue")
    scrollbar = Scrollbar(frame_guess, command=textarea_guess.yview)
    scrollbar.grid(row=0, column=1, sticky='nsew')
    textarea_guess['yscrollcommand'] = scrollbar.set

    frame_final = Frame(root, relief=RAISED, borderwidth=1)
    frame_final.pack(fill=X, padx=0, pady=0)
    status_label = Label(frame_final, text="Status: relax",
                         anchor='w', width=15, fg="blue")
    status_label.pack(side=LEFT, padx=10, pady=0)

    frame_notification_5 = Frame(root, relief=RAISED, borderwidth=1)
    frame_notification_5.pack(fill=X, padx=0, pady=0)

    textarea = Text(frame_notification_5, width=57, height=10)
    textarea.pack(side=LEFT, padx=10, pady=10)
    textarea.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    textarea.tag_config('lost', foreground="red")
    textarea.tag_config('win', foreground="green")

    scrollbar = Scrollbar(frame_notification_5, command=textarea.yview)
    scrollbar.grid(row=0, column=1, sticky='nsew')
    textarea['yscrollcommand'] = scrollbar.set

    ra = open("./data/rs.txt", "r")
    dataRs = ra.read()
    ra.close()
    textarea_guess.insert(END, dataRs)

    dataRe = dataRs.split("\n")
    dataRa = textarea_guess.get("1.0", END).split("\n")
    arrBet = []
    arrwl = []
    noBet = 0

    imageG = Image.open("./images/green.png")
    imageG = imageG.resize((15, 15), Image.ANTIALIAS)
    photoImgG = ImageTk.PhotoImage(imageG)
    imageR = Image.open("./images/red.png")
    imageR = imageR.resize((15, 15), Image.ANTIALIAS)
    photoImgR = ImageTk.PhotoImage(imageR)
    imageY = Image.open("./images/yellow.png")
    imageY = imageY.resize((15, 15), Image.ANTIALIAS)
    photoImgY = ImageTk.PhotoImage(imageY)

    def reset_predict():
        textarea_guess.delete('1.0', END)
        textarea_guess.insert(END, dataRs)

    def login():
        global driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome("chromedriver.exe", options=options)
        driver.get("https://bc.game/crash/trenball")

    def replaceData(runing, choice):
        textarea_guess.delete('1.0', END)
        for num in range(len(dataRe)):
            textarea_guess.insert(END, str(arrwl[num][0]), "win")
            textarea_guess.insert(END, "-")
            textarea_guess.insert(END, str(arrwl[num][1]), "lost")
            textarea_guess.insert(END, "-")
            if(choice == 1):
                textarea_guess.insert(END, str(arrBet[num]))
                textarea_guess.insert(END, "-")
            if(num == runing):
                textarea_guess.insert(END, str(dataRe[num])+"\n", "run")
                textarea_guess.see(str(num+1)+".0")
            else:
                textarea_guess.insert(END, str(dataRe[num])+"\n")

    def handingNumber(value):
        if(value >= 1 and value < 2):
            return "R"
        elif(value >= 2 and value < 10):
            return "G"
        else:
            return "Y"
    def get_time(start):
        timeRunSec=time.time()-start
        minutes=timeRunSec/60
        seconds=math.floor(
            0.6*((minutes*100) % 100))
        minutes=math.floor(minutes)
        return [minutes, seconds]

    def getnext(arr, choice):
        stringArr = arr
        if(stringArr[len(stringArr)-1] != "Y" and "Y" in stringArr and choice == 1):
            stringArr = stringArr.replace("Y", "G")
        for num in range(len(dataRa)):
            if(dataRa[num] != ""):
                if(dataRa[num][:len(dataRa[num])-2] == stringArr[(len(stringArr) - (len(dataRa[num])-2)):]):
                    return [dataRa[num][len(dataRa[num])-1], num]
            else:
                break
        return ["N", 0]

    def chng_image_history(arr):
        for i in range(len(arr)):
            if(arr[i] == "G"):
                history_label[i].config(image=photoImgG)
                history_label[i].photo_ref = photoImgG
            elif(arr[i] == "R"):
                history_label[i].config(image=photoImgR)
                history_label[i].photo_ref = photoImgR
            if(arr[i] == "Y"):
                history_label[i].config(image=photoImgY)
                history_label[i].photo_ref = photoImgY

    def chng_image(photo):
        image_label.config(image=photo)
        image_label.photo_ref = photo

    def get_balance():
        return float(driver.find_element_by_xpath(
            "/html/body/div["+str(numElement+1)+"]/div/div[2]/div[1]/div/div/div[2]/div/span").get_attribute('textContent'))

    def get_his_payout(num):
        return float(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div["+str(
            num)+"]/div[2]").get_attribute('textContent').replace("x", ""))
    
    def get_len_current():
        return len(driver.find_elements_by_xpath(
            "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div"))

    def get_input_b():
        return driver.find_elements_by_xpath(
            """//*[@class="input-control"]/input[@type="text"]""")

    def click_button_bet(num):
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div["+str(num)+"]/button/div").click()

    def get_default_bet():
        if(value_checkbox_bet_by_balace.get() == 0):
            return float(input_bet.get())
        else:
            for numElement in range(11):
                try:
                    balance = get_balance()
                    multiply = int(input_multiple_balance.get())
                    newBet = round(float(balance/multiply), 8)
                    input_bet.delete(0, END)
                    input_bet.insert(0, str(newBet))
                    return newBet
                    break
                except:
                    balance = 0
            return float(input_bet.get())
    

    def rule():
        imageG = Image.open("./images/green.png")
        imageG = imageG.resize((15, 15), Image.ANTIALIAS)
        photoImgG = ImageTk.PhotoImage(imageG)
        imageR = Image.open("./images/red.png")
        imageR = imageR.resize((15, 15), Image.ANTIALIAS)
        photoImgR = ImageTk.PhotoImage(imageR)
        vcr = value_checkbox_replace.get()
        vcspm = value_checkbox_separate_prediction_money.get()
        timeChangeBet = int(input_min_cal.get())
        vcp = value_checkbox_pause.get()
        try:
            driver.find_element_by_xpath(
                "/html/body/div[2]/button/div").click()
        except:
            pass
        try:
            status_label.config(fg="green")
            status_label["text"] = "Status: runing"
            timeRun = 0
            timeBet = 0
            timeWin = 0
            timeLost = 0
            lastPayout = 0
            payout = 0
            profit = 0
            balance = get_balance()
            percent_pause = input_percent.get()
            profit_pause = round(balance/percent_pause,8)
            betMain = get_default_bet()
            bet = betMain
            payouting = 2
            stopLost = float(input_sl.get())*(-1)
            takeProfit = float(input_tp.get())
            check2 = True
            lostPr = 0
            winP = 0
            maxBet = bet
            timeStart = time.time()
            realTime = []
            lineNoti = 0
            for i in range(len(dataRa)):
                arrBet.append(bet)
                arrwl.append([0, 0])
            gOr = "N"
            gOrImage = photoImgR
            currentBet = []
            inputB = get_input_b()

            lengthCurrent = get_len_current()
            try:
                historyValue = handingNumber(get_his_payout(lengthCurrent-5)) + \
                    handingNumber(get_his_payout(lengthCurrent-4)) + \
                    handingNumber(get_his_payout(lengthCurrent-3)) + \
                    handingNumber(get_his_payout(lengthCurrent-2)) + \
                    handingNumber(get_his_payout(lengthCurrent-1)) + \
                    handingNumber(get_his_payout(lengthCurrent))

            except:
                historyValue = handingNumber(get_his_payout(lengthCurrent-2)) + \
                    handingNumber(get_his_payout(lengthCurrent-1)) + \
                    handingNumber(get_his_payout(lengthCurrent))
            lastPayout = get_his_payout(lengthCurrent)
            while True:
                check2=True
                try:
                    check=True
                    payout=float(get_his_payout(lengthCurrent))
                    if(lastPayout != payout):
                        timeRun += 1
                        if(len(historyValue) == 7):
                            historyValue=historyValue[1:]
                        historyValue += (handingNumber(payout))
                        lastPayout=payout
                        currentBet=getnext(historyValue, vcr)
                        gOr=currentBet[0]
                        noBet=currentBet[1]
                        chng_image_history(historyValue)
                        last_payout_label["text"]=str(lastPayout)
                        if(gOr != "N"):
                            if(vcspm == 1):
                                bet=arrBet[noBet]
                            else:
                                bet=arrBet[0]
                            if(timeRun != 1):
                                ActionChains(driver).click(inputB[0]).key_down(Keys.CONTROL).send_keys(
                                    "a").key_up(Keys.CONTROL).send_keys(str("%.8f"%(bet))).perform()
                                time.sleep(3)
                                try:
                                    if(gOr == "R"):
                                        betBut=click_button_bet(2)
                                        payouting=1.96
                                        gOrImage=photoImgR
                                    elif(gOr == "G"):
                                        betBut=click_button_bet(3)
                                        payouting=2
                                        gOrImage=photoImgG
                                    chng_image(photoImgG)
                                except:
                                    textarea.insert(
                                        END, str(timeRun) + ".Bet: 0.00000000 - Can not Click" + "\n", "lost")
                                    driver.refresh()
                                    lengthCurrent=0
                                    while(lengthCurrent == 0):
                                        try:
                                            lengthCurrent=get_len_current()
                                            inputB=get_input_b()
                                        except:
                                            lengthCurrent=0
                                            time.sleep(0.5)
                                    check2=False
                                if(check2):
                                    timeBet += 1
                                    beting_label["text"]=str(bet)
                                    textarea.insert(
                                        END, str(timeRun) + ".Bet: %.8f" % (bet) + " - ")
                                    textarea.image_create(
                                        END, image=gOrImage)
                                    replaceData(noBet, vcspm)
                                    while True:
                                        payout2=float(get_his_payout(lengthCurrent))
                                        if(payout2 != lastPayout):
                                            if((payout2 < 2 and gOr == "R") or (payout2 >= 2 and gOr == "G")):
                                                arrwl[noBet][0]=arrwl[noBet][0]+1
                                                winP=round(
                                                    bet*(payouting-1), 8)
                                                profit_pause -= winP
                                                profit += winP
                                                textarea.insert(
                                                    END, " - Win", "win")
                                                textarea.insert(
                                                    END, " - Payout: " + str(payout2) + "\n")
                                                bet=betMain
                                                timeWin += 1
                                                time_win_label["text"]=str(
                                                    timeWin)
                                            else:
                                                arrwl[noBet][1]=arrwl[noBet][1]+1
                                                lostPr=bet
                                                profit -= lostPr
                                                profit_pause+=lostPr
                                                textarea.insert(
                                                    END, " - Lose", "lost")
                                                textarea.insert(
                                                    END, " - Payout: " + str(payout2) + "\n")
                                                bet=bet *2.05
                                                bet=round(bet, 8)
                                                if(bet > maxBet):
                                                    maxBet=bet
                                                    textarea.insert(
                                                        END, "====> New biggest bet: %.8f\n" % (maxBet), "lost")
                                                    if(vcspm == 1):
                                                        bet_max_label["text"]=str(
                                                            maxBet)
                                                        with_prediction_label["text"]=dataRe[noBet]
                                                    else:
                                                        bet_max_label["text"]=str(
                                                            maxBet)
                                                        with_prediction_label["text"]=""
                                                timeLost += 1
                                                time_lost_label["text"]=str(
                                                    timeLost)
                                            if(vcp == 1):
                                                if(profit_pause <= 0):
                                                    realTime = get_time(timeStart)
                                                    time_label["text"]=str(
                                                        realTime[0]) + ":" + str(realTime[1])

                                                    
                                            if(vcspm == 1):
                                                arrBet[noBet]=bet
                                            else:
                                                arrBet[0]=bet
                                            replaceData(noBet, vcspm)
                                            break
                                        else:
                                            time.sleep(0.3)
                                        realTime = get_time(timeStart)
                                        time_label["text"]=str(
                                            realTime[0]) + ":" + str(realTime[1])
                                        if(realTime[0] % 60 == 0):
                                            betMain=get_default_bet()
                            if(profit >= 0):
                                profit_label.config(fg="green")
                                profit_label_title.config(fg="green")
                            else:
                                profit_label.config(fg="red")
                                profit_label_title.config(fg="red")
                            profit_label["text"]=str(round(profit, 8))
                            time_bet_label["text"]=str(timeBet)
                            if(profit-bet <= stopLost or profit >= takeProfit):
                                textarea.insert(
                                    END, "Stop win or lost" + "\n", "lost")
                                break
                        else:
                            beting_label["text"]="0"
                            textarea.insert(
                                END, str(timeRun) + ".Bet: 0.00000000 - Pass this time" + "\n")
                        time_run_label["text"]=str(timeRun)
                        textarea.see(END)
                        lineNoti=int(textarea.index(
                            'end-1c').split('.')[0])
                        if(lineNoti >= 100):
                            textarea.delete(
                                "1.0", (str(lineNoti-100+2)+".0"))
                    else:
                        time.sleep(0.3)
                    realTime = get_time(timeStart)
                    time_label["text"]=str(
                        realTime[0]) + ":" + str(realTime[1])
                except Exception as e:
                    textarea.insert(END, "Stop breaking!" + "\n", "lost")
                    textarea.insert(END, e)
                    textarea.insert(END, "\n", "lost")
                    textarea.insert(END, "__________________" + "\n", "lost")
                    status_label.config(fg="red")
                    status_label["text"]="Status: break"
                    textarea.see(END)
                    break
        except Exception as e:
            status_label.config(fg="red")
            textarea.insert(END, e)
            textarea.insert(END, "\n", "lost")
            status_label["text"]="Status: fail"
            textarea.see(END)

    def run():
        global t
        t=threading.Thread(target=rule).start()

    login_button=Button(frame1, text="Login", command=login)
    login_button.pack(side=RIGHT, padx=5, pady=0)
    reset_predict_button=Button(
        frame_guess_setting_2, text="Reset prediction", command=reset_predict)
    reset_predict_button.pack(side=RIGHT, padx=5, pady=0)
    start_button=Button(frame_final, text="Start Bet", command=run)
    start_button.pack(side=RIGHT, padx=5, pady=5)

    root.mainloop()

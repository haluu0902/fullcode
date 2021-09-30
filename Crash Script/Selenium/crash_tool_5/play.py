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


class auto_run(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.set_default_value()

    def initUI(self):
        self.parent.title("Auto Crash Trendball BC.Game - By: SaviorXXI")
        img = tk.Image("photo", file="./images/icon.png")
        self.parent.iconbitmap(r'./images/icon.ico')
        self.parent.resizable(0, 0)
        self.parent.tk.call('wm', 'iconphoto', self.parent._w, img)

        self.frame1 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame1.pack(fill=X, padx=0, pady=0)

        bet_label = Label(self.frame1, text="Bet:", anchor='w', width=10)
        bet_label.pack(side=LEFT, padx=10, pady=0)
        self.value_bet = StringVar(self.parent, value='10')
        self.input_bet = Entry(self.frame1, width=10,
                               textvariable=self.value_bet)
        self.input_bet.pack(side=LEFT, padx=2, pady=0)

        self.value_checkbox_bet_by_balace = IntVar(value=1)
        self.checkbox_bet_by_balace = Checkbutton(
            self.frame1, text='Bet by dividing the balance', variable=self.value_checkbox_bet_by_balace)
        self.checkbox_bet_by_balace.pack(side=LEFT, padx=0, pady=0)

        self.value_input_multiple_balance = StringVar(
            self.parent, value='650')
        self.input_multiple_balance = Entry(
            self.frame1, width=10, textvariable=self.value_input_multiple_balance)
        self.input_multiple_balance.pack(side=LEFT, padx=0, pady=0)

        self.frame2 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame2.pack(fill=X, padx=0, pady=0)

        tp_label = Label(self.frame2, text="Take Profit:",
                         anchor='w', width=10)
        tp_label.pack(side=LEFT, padx=10, pady=0)
        self.value_tp = StringVar(self.parent, value='1000')
        self.input_tp = Entry(self.frame2, width=10,
                              textvariable=self.value_tp)
        self.input_tp.pack(side=LEFT, padx=0, pady=0)

        sl_label = Label(self.frame2, text="Stop Lost:", anchor='w', width=17)
        sl_label.pack(side=LEFT, padx=25, pady=0)
        self.value_sl = StringVar(self.parent, value='1000')
        self.input_sl = Entry(self.frame2, textvariable=self.value_sl, width = 10)
        self.input_sl.pack(side=LEFT, padx=0, pady=0)

        self.frame_notification_1 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_notification_1.pack(fill=X, padx=0, pady=0)

        history_title = Label(
            self.frame_notification_1, text="History: ", anchor='w', width=10)
        history_title.pack(side=LEFT, padx=10, pady=0)

        self.history_1 = Label(self.frame_notification_1, anchor='w')
        self.history_1.pack(side=LEFT, padx=0, pady=0)
        self.history_2 = Label(self.frame_notification_1, anchor='w')
        self.history_2.pack(side=LEFT, padx=0, pady=0)
        self.history_3 = Label(self.frame_notification_1, anchor='w')
        self.history_3.pack(side=LEFT, padx=0, pady=0)
        self.history_4 = Label(self.frame_notification_1, anchor='w')
        self.history_4.pack(side=LEFT, padx=0, pady=0)
        self.history_5 = Label(self.frame_notification_1, anchor='w')
        self.history_5.pack(side=LEFT, padx=0, pady=0)
        self.history_6 = Label(self.frame_notification_1, anchor='w')
        self.history_6.pack(side=LEFT, padx=0, pady=0)
        self.history_7 = Label(self.frame_notification_1, anchor='w')
        self.history_7.pack(side=LEFT, padx=0, pady=0)
        self.history_8 = Label(self.frame_notification_1, anchor='w')
        self.history_8.pack(side=LEFT, padx=0, pady=0)
        self.history_9 = Label(self.frame_notification_1, anchor='w')
        self.history_9.pack(side=LEFT, padx=0, pady=0)
        self.history_10 = Label(self.frame_notification_1, anchor='w')
        self.history_10.pack(side=LEFT, padx=0, pady=0)
        self.history_11 = Label(self.frame_notification_1, anchor='w')
        self.history_11.pack(side=LEFT, padx=0, pady=0)
        self.history_12 = Label(self.frame_notification_1, anchor='w')
        self.history_12.pack(side=LEFT, padx=0, pady=0)

        self.history_label = [self.history_1, self.history_2, self.history_3,
                              self.history_4, self.history_5, self.history_6, self.history_7,
                              self.history_8, self.history_9, self.history_10,
                              self.history_11, self.history_12]

        self.frame_notification_2 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_notification_2.pack(fill=X, padx=0, pady=0)

        last_payout_label_title = Label(self.frame_notification_2,
                                        text="Last payout: ", anchor='w', width=10)
        last_payout_label_title.pack(fill=X, side=LEFT, padx=10, pady=0)

        self.last_payout_label = Label(self.frame_notification_2,
                                       text="0.0", anchor='w', width=10)
        self.last_payout_label.pack(fill=X, side=LEFT, padx=0, pady=0)

        self.frame_notification_2_1 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_notification_2_1.pack(fill=X, padx=0, pady=0)

        beting_label_title = Label(self.frame_notification_2_1,
                                   text="Bet: ", anchor='w', width=10)
        beting_label_title.pack(side=LEFT, padx=10, pady=0)

        self.beting_label = Label(self.frame_notification_2_1,
                                  text="0.00000000", anchor='w', width=20)
        self.beting_label.pack(side=LEFT, padx=0, pady=0)

        image_label_title = Label(self.frame_notification_2_1,
                                  anchor='w', text="Bet color:", width=10)
        image_label_title.pack(side=LEFT, padx=0, pady=0)

        self.image_label = Label(self.frame_notification_2_1, anchor='w')
        self.image_label.pack(side=LEFT, padx=0, pady=0)

        self.frame_notification_2_2 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_notification_2_2.pack(fill=X, padx=0, pady=0)

        bet_max_label_title = Label(
            self.frame_notification_2_2, text="Biggest bet: ", anchor='w', width=10)
        bet_max_label_title.pack(side=LEFT, padx=10, pady=0)

        self.bet_max_label = Label(
            self.frame_notification_2_2, text="0.00000000", anchor='w', width=20)
        self.bet_max_label.pack(side=LEFT, padx=0, pady=0)

        with_prediction_label_title = Label(
            self.frame_notification_2_2, text="From: ", anchor='w', width=10)
        with_prediction_label_title.pack(side=LEFT, padx=0, pady=0)

        self.with_prediction_label = Label(
            self.frame_notification_2_2, text="GGGGGGG-G", anchor='w', width=10)
        self.with_prediction_label.pack(side=LEFT, padx=0, pady=0)

        self.frame_notification_3 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_notification_3.pack(fill=X, padx=0, pady=0)

        time_run_label_title = Label(self.frame_notification_3,
                                     text="Time run: ", anchor='w', width=10)
        time_run_label_title.pack(side=LEFT, padx=10, pady=0)

        self.time_run_label = Label(self.frame_notification_3,
                                    text="0", anchor='w', width=20)
        self.time_run_label.pack(side=LEFT, padx=0, pady=0)

        time_bet_label_title = Label(self.frame_notification_3,
                                     text="Time bet: ", anchor='w', width=10)
        time_bet_label_title.pack(side=LEFT, padx=0, pady=0)

        self.time_bet_label = Label(self.frame_notification_3,
                                    text="0", anchor='w', width=10)
        self.time_bet_label.pack(side=LEFT, padx=0, pady=0)

        self.frame_notification_4 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_notification_4.pack(fill=X, padx=0, pady=0)

        time_win_label_title = Label(
            self.frame_notification_4, text="Time win: ", anchor='w', width=10, fg="green")
        time_win_label_title.pack(side=LEFT, padx=10, pady=0)

        self.time_win_label = Label(
            self.frame_notification_4, text="0", anchor='w', width=20, fg="green")
        self.time_win_label.pack(side=LEFT, padx=0, pady=0)

        time_lost_label_title = Label(
            self.frame_notification_4, text="Time lost: ", anchor='w', width=10, fg="red")
        time_lost_label_title.pack(side=LEFT, padx=0, pady=0)

        self.time_lost_label = Label(
            self.frame_notification_4, text="0", anchor='w', width=10, fg="red")
        self.time_lost_label.pack(side=LEFT, padx=0, pady=0)

        self.frame_notification_4_1 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_notification_4_1.pack(fill=X, padx=0, pady=0)

        self.profit_label_title = Label(
            self.frame_notification_4_1, text="Profit: ", anchor='w', width=10, fg="green")
        self.profit_label_title.pack(side=LEFT, padx=10, pady=0)

        self.profit_label = Label(
            self.frame_notification_4_1, text="0.00000000", anchor='w', width=20, fg="green")
        self.profit_label.pack(side=LEFT, padx=0, pady=0)

        time_label_title = Label(self.frame_notification_4_1,
                                 text="Time running: ", anchor='w', width=10)
        time_label_title.pack(side=LEFT, padx=00, pady=0)

        self.time_label = Label(self.frame_notification_4_1,
                                text="0:0", anchor='w', width=10)
        self.time_label.pack(side=LEFT, padx=0, pady=0)

        self.frame1_1 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame1_1.pack(fill=X, padx=0, pady=0)

        self.value_checkbox_cal_every_min = IntVar(value=1)
        checkbox_cal_every_min = Checkbutton(
            self.frame1_1, text='Calculate bet by balance again every', variable=self.value_checkbox_cal_every_min)
        checkbox_cal_every_min.pack(side=LEFT, padx=10, pady=0)

        self.value_input_min_cal = StringVar(self.parent, value='60')
        self.input_min_cal = Entry(
            self.frame1_1, width=5, textvariable=self.value_input_min_cal)
        self.input_min_cal.pack(side=LEFT, padx=0, pady=0)

        minutes_label = Label(self.frame1_1, text="minutes")
        minutes_label.pack(side=LEFT, padx=0, pady=0)

        self.frame1_1_1 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame1_1_1.pack(fill=X, padx=0, pady=0)

        self.value_checkbox_pause = IntVar(value=1)
        checkbox_pause = Checkbutton(
            self.frame1_1_1, text='Pause to next hour when get', variable=self.value_checkbox_pause)
        checkbox_pause.pack(side=LEFT, padx=10, pady=0)

        self.value_input_percent = StringVar(self.parent, value='2')
        self.input_percent = Entry(
            self.frame1_1_1, width=5, textvariable=self.value_input_percent)
        self.input_percent.pack(side=LEFT, padx=0, pady=0)

        percent_label = Label(self.frame1_1_1, text="percent balance")
        percent_label.pack(side=LEFT, padx=0, pady=0)

        self.frame_guess_setting_1 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_guess_setting_1.pack(fill=X, padx=0, pady=0)

        self.value_checkbox_replace = IntVar(value=1)
        checkbox_replace = Checkbutton(
            self.frame_guess_setting_1, text='Replace Y = G when results do not match', variable=self.value_checkbox_replace)
        checkbox_replace.pack(side=LEFT, padx=10, pady=0)

        self.frame_guess_setting_2 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_guess_setting_2.pack(fill=X, padx=0, pady=0)

        self.value_checkbox_separate_prediction_money = IntVar(value=0)
        checkbox_separate_prediction_money = Checkbutton(
            self.frame_guess_setting_2, text='Separation of prediction and money', variable=self.value_checkbox_separate_prediction_money)
        checkbox_separate_prediction_money.pack(side=LEFT, padx=10, pady=0)

        self.frame_guess = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame_guess.pack(fill=X, padx=0, pady=0)
        self.textarea_guess = Text(self.frame_guess, width=55, height=5)
        self.textarea_guess.pack(side=LEFT, padx=10, pady=10)
        self.textarea_guess.grid(
            row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.textarea_guess.tag_config('lost', foreground="red")
        self.textarea_guess.tag_config('win', foreground="green")
        bold_font = font.Font(self.textarea_guess,
                              self.textarea_guess.cget("font"))
        bold_font.configure(weight="bold")
        self.textarea_guess.tag_configure(
            "run", font=bold_font, foreground="blue")
        scrollbar = Scrollbar(
            self.frame_guess, command=self.textarea_guess.yview)
        scrollbar.grid(row=0, column=1, sticky='nsew')
        self.textarea_guess['yscrollcommand'] = scrollbar.set

        self.frame_final = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame_final.pack(fill=X, padx=0, pady=0)
        self.status_label = Label(self.frame_final, text="Status: relax",
                                  anchor='w', width=30, fg="purple")
        self.status_label.pack(side=LEFT, padx=10, pady=0)

        self.frame_notification_5 = Frame(
            self.parent, relief=RAISED, borderwidth=1)
        self.frame_notification_5.pack(fill=X, padx=0, pady=0)

        self.textarea = Text(self.frame_notification_5, width=55, height=10)
        self.textarea.pack(side=LEFT, padx=10, pady=10)
        self.textarea.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.textarea.tag_config('lost', foreground="red")
        self.textarea.tag_config('win', foreground="green")

        scrollbar = Scrollbar(self.frame_notification_5,
                              command=self.textarea.yview)
        scrollbar.grid(row=0, column=1, sticky='nsew')
        self.textarea['yscrollcommand'] = scrollbar.set

        login_button = Button(self.frame1, text="Login", command=self.login)
        login_button.pack(side=RIGHT, padx=5, pady=0)
        reset_predict_button = Button(
            self.frame_guess_setting_2, text="Reset prediction", command=self.reset_predict)
        reset_predict_button.pack(side=RIGHT, padx=5, pady=0)
        start_button = Button(
            self.frame_final, text="Start Bet", command=self.run)
        start_button.pack(side=RIGHT, padx=5, pady=5)

    def set_default_value(self):
        self.imageG = Image.open("./images/green.png")
        self.imageG = self.imageG.resize((15, 15), Image.ANTIALIAS)
        self.photoImgG = ImageTk.PhotoImage(self.imageG)
        self.imageR = Image.open("./images/red.png")
        self.imageR = self.imageR.resize((15, 15), Image.ANTIALIAS)
        self.photoImgR = ImageTk.PhotoImage(self.imageR)
        self.imageY = Image.open("./images/yellow.png")
        self.imageY = self.imageY.resize((15, 15), Image.ANTIALIAS)
        self.photoImgY = ImageTk.PhotoImage(self.imageY)
        ra = open("./data/rs.txt", "r")
        self.dataRs = ra.read()
        ra.close()
        self.textarea_guess.insert(END, self.dataRs)
        self.dataRe = self.dataRs.split("\n")
        self.dataRa = self.textarea_guess.get("1.0", END).split("\n")
        self.arrBet = []
        self.arrwl = []
        self.noBet = 0

    def reset_predict(self):
        self.textarea_guess.delete('1.0', END)
        self.textarea_guess.insert(END, self.dataRs)

    def login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        self.driver.get("https://bc.game/crash/trenball")

    def replaceData(self, runing, choice):
        self.textarea_guess.delete('1.0', END)
        for num in range(len(self.dataRe)):
            self.textarea_guess.insert(END, str(self.arrwl[num][0]), "win")
            self.textarea_guess.insert(END, "-")
            self.textarea_guess.insert(END, str(self.arrwl[num][1]), "lost")
            self.textarea_guess.insert(END, "-")
            if(choice == 1):
                self.textarea_guess.insert(END, str(self.arrBet[num]))
                self.textarea_guess.insert(END, "-")
            if(num == runing):
                self.textarea_guess.insert(
                    END, str(self.dataRe[num])+"\n", "run")
                self.textarea_guess.see(str(num+1)+".0")
            else:
                self.textarea_guess.insert(END, str(self.dataRe[num])+"\n")

    def handingNumber(self, value):
        if(value >= 1 and value < 2):
            return "R"
        elif(value >= 2 and value < 10):
            return "G"
        else:
            return "Y"

    def get_time(self, start):
        timeRunSec = time.time()-start
        minutes = timeRunSec/60
        seconds = math.floor(
            0.6*((minutes*100) % 100))
        minutes = math.floor(minutes)
        return [minutes, seconds]

    def getnext(self, arr, choice):
        stringArr = arr
        if(stringArr[len(stringArr)-1] != "Y" and "Y" in stringArr and choice == 1):
            stringArr = stringArr.replace("Y", "G")
        for num in range(len(self.dataRa)):
            if(self.dataRa[num] != ""):
                if(self.dataRa[num][:len(self.dataRa[num])-2] == stringArr[(len(stringArr) - (len(self.dataRa[num])-2)):]):
                    return [self.dataRa[num][len(self.dataRa[num])-1], num]
            else:
                break
        return ["N", 0]

    def chng_image_history(self, arr):
        for i in range(len(arr)):
            if(arr[i] == "G"):
                self.history_label[i].config(image=self.photoImgG)
                self.history_label[i].photo_ref = self.photoImgG
            elif(arr[i] == "R"):
                self.history_label[i].config(image=self.photoImgR)
                self.history_label[i].photo_ref = self.photoImgR
            if(arr[i] == "Y"):
                self.history_label[i].config(image=self.photoImgY)
                self.history_label[i].photo_ref = self.photoImgY

    def chng_image(self, photo):
        self.image_label.config(image=photo)
        self.image_label.photo_ref = photo

    def get_balance(self):
        for numElement in range(11):
            try:
                balance = float(self.driver.find_element_by_xpath(
                    "/html/body/div["+str(numElement+1)+"]/div/div[2]/div[1]/div/div/div[2]/div/span").get_attribute('textContent'))
                return balance
            except:
                balance = 0
        return balance

    def get_his_payout(self, num):
        return float(self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div["+str(
            num)+"]/div[2]").get_attribute('textContent').replace("x", ""))

    def get_len_current(self):
        return len(self.driver.find_elements_by_xpath(
            "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div"))

    def get_input_b(self):
        return self.driver.find_elements_by_xpath(
            """//*[@class="input-control"]/input[@type="text"]""")

    def click_button_bet(self, num):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div["+str(num)+"]/button/div").click()

    def get_default_bet(self):
        if(self.value_checkbox_bet_by_balace.get() == 0):
            return float(self.input_bet.get())
        else:
            balance = self.get_balance()
            if(balance != 0):
                multiply = int(self.input_multiple_balance.get())
                newBet = round(float(balance/multiply), 8)
                self.input_bet.delete(0, END)
                self.input_bet.insert(0, str(newBet))
                return newBet
            else:
                return float(self.input_bet.get())

    def get_history_first(self, lengthCurrent):
        try:
            historyValue = self.handingNumber(self.get_his_payout(lengthCurrent-5)) + \
                self.handingNumber(self.get_his_payout(lengthCurrent-4)) + \
                self.handingNumber(self.get_his_payout(lengthCurrent-3)) + \
                self.handingNumber(self.get_his_payout(lengthCurrent-2)) + \
                self.handingNumber(self.get_his_payout(lengthCurrent-1)) + \
                self.handingNumber(self.get_his_payout(lengthCurrent))

        except:
            historyValue = self.handingNumber(self.get_his_payout(lengthCurrent-2)) + \
                self.handingNumber(self.get_his_payout(lengthCurrent-1)) + \
                self.handingNumber(self.get_his_payout(lengthCurrent))
        return historyValue

    def rule(self):
        vcr = self.value_checkbox_replace.get()
        vcspm = self.value_checkbox_separate_prediction_money.get()
        timeChangeBet = int(self.input_min_cal.get())
        vcp = self.value_checkbox_pause.get()
        try:
            self.driver.find_element_by_xpath(
                "/html/body/div[2]/button/div").click()
        except:
            pass
        try:
            self.status_label.config(fg="green")
            self.status_label["text"] = "Status: runing"
            balance = self.get_balance()
            percent_pause = int(self.input_percent.get())
            profit_pause = round(balance/100*percent_pause, 8)
            betMain = self.get_default_bet()
            stopLost = float(self.input_sl.get())*(-1)
            takeProfit = float(self.input_tp.get())
            timeStart = time.time()
            lengthCurrent = self.get_len_current()
            historyValue = self.get_history_first(lengthCurrent)
            lastPayout = self.get_his_payout(lengthCurrent)
            check2 = True
            gOr = "N"
            bet = betMain
            payouting = 2
            maxBet = bet
            realTime = []
            currentBet = []
            gOrImage = self.photoImgR
            inputB = self.get_input_b()
            lineNoti, timeRun, timeBet, timeWin, timeLost, payout, profit, winP, lostPr, = 0, 0, 0, 0, 0, 0, 0, 0, 0
            for i in range(len(self.dataRa)):
                self.arrBet.append(bet)
                self.arrwl.append([0, 0])
            while True:
                check2 = True
                try:
                    check = True
                    payout = self.get_his_payout(lengthCurrent)
                    if(lastPayout != payout):
                        timeRun += 1
                        if(len(historyValue) == 12):
                            historyValue = historyValue[1:]
                        historyValue += (self.handingNumber(payout))
                        lastPayout = payout
                        currentBet = self.getnext(historyValue, vcr)
                        gOr = currentBet[0]
                        noBet = currentBet[1]
                        self.chng_image_history(historyValue)
                        self.last_payout_label["text"] = str(lastPayout)
                        if(gOr != "N"):
                            if(vcspm == 1):
                                bet = self.arrBet[noBet]
                            else:
                                bet = self.arrBet[0]
                            if(timeRun != 1):
                                ActionChains(self.driver).click(inputB[0]).key_down(Keys.CONTROL).send_keys(
                                    "a").key_up(Keys.CONTROL).send_keys(str("%.8f" % (bet))).perform()
                                time.sleep(3)
                                try:
                                    if(gOr == "R"):
                                        betBut = 2
                                        payouting = 1.96
                                        gOrImage = self.photoImgR
                                    elif(gOr == "G"):
                                        betBut = 3
                                        payouting = 2
                                        gOrImage = self.photoImgG
                                    self.click_button_bet(betBut)
                                    self.chng_image(self.photoImgG)
                                except:
                                    self.textarea.insert(
                                        END, str(timeRun) + ".Bet: 0.00000000 - Can not Click" + "\n", "lost")
                                    self.driver.refresh()
                                    lengthCurrent = 0
                                    while(lengthCurrent == 0):
                                        try:
                                            lengthCurrent = self.get_len_current()
                                            inputB = self.get_input_b()
                                        except:
                                            lengthCurrent = 0
                                            time.sleep(0.5)
                                    check2 = False
                                if(check2):
                                    timeBet += 1
                                    self.beting_label["text"] = str(bet)
                                    self.textarea.insert(
                                        END, str(timeRun) + ".Bet: %.8f" % (bet) + " - ")
                                    self.textarea.image_create(
                                        END, image=gOrImage)
                                    self.replaceData(noBet, vcspm)
                                    while True:
                                        payout2 = self.get_his_payout(
                                            lengthCurrent)
                                        if(payout2 != lastPayout):
                                            if((payout2 < 2 and gOr == "R") or (payout2 >= 2 and gOr == "G")):
                                                self.arrwl[noBet][0] = self.arrwl[noBet][0]+1
                                                winP = round(
                                                    bet*(payouting-1), 8)
                                                profit_pause -= winP
                                                profit += winP
                                                self.textarea.insert(
                                                    END, " - Win", "win")
                                                self.textarea.insert(
                                                    END, " - Payout: " + str(payout2) + "\n")
                                                bet = betMain
                                                timeWin += 1
                                                self.time_win_label["text"] = str(
                                                    timeWin)
                                            else:
                                                self.arrwl[noBet][1] = self.arrwl[noBet][1]+1
                                                lostPr = bet
                                                profit -= lostPr
                                                profit_pause += lostPr
                                                self.textarea.insert(
                                                    END, " - Lose", "lost")
                                                self.textarea.insert(
                                                    END, " - Payout: " + str(payout2) + "\n")
                                                bet = bet * 2.05
                                                bet = round(bet, 8)
                                                if(bet > maxBet):
                                                    maxBet = bet
                                                    self.textarea.insert(
                                                        END, "====> New biggest bet: %.8f\n" % (maxBet), "lost")
                                                    if(vcspm == 1):
                                                        self.bet_max_label["text"] = str(
                                                            maxBet)
                                                        self.with_prediction_label["text"] = dataRe[noBet]
                                                    else:
                                                        self.bet_max_label["text"] = str(
                                                            maxBet)
                                                        self.with_prediction_label["text"] = ""
                                                timeLost += 1
                                                self.time_lost_label["text"] = str(
                                                    timeLost)
                                            if(vcp == 1):
                                                if(profit_pause <= 0):
                                                    self.textarea.insert(
                                                        END, "===> Win enough. Relax now ^^" + "\n", "win")
                                                    self.status_label.config(fg="purple")
                                                    self.status_label["text"] = "Status: Take some coffee ^^"
                                                    realTime = self.get_time(
                                                        timeStart)
                                                    oldHour = math.floor(
                                                        realTime[0]/60)
                                                    while(math.floor(realTime[0]/60) == oldHour):
                                                        realTime = self.get_time(
                                                            timeStart)
                                                        self.time_label["text"] = str(
                                                            realTime[0]) + ":" + str(realTime[1])
                                                        time.sleep(0.2)
                                                    betMain = self.get_default_bet()
                                            if(vcspm == 1):
                                                self.arrBet[noBet] = bet
                                            else:
                                                self.arrBet[0] = bet
                                            self.replaceData(noBet, vcspm)
                                            break
                                        else:
                                            time.sleep(0.3)
                                        realTime = self.get_time(timeStart)
                                        self.time_label["text"] = str(
                                            realTime[0]) + ":" + str(realTime[1])
                                        if(realTime[0] % 60 == 0 and realTime[0] != 0):
                                            betMain = self.get_default_bet()
                            if(profit >= 0):
                                self.profit_label.config(fg="green")
                                self.profit_label_title.config(fg="green")
                            else:
                                self.profit_label.config(fg="red")
                                self.profit_label_title.config(fg="red")
                            self.profit_label["text"] = str(round(profit, 8))
                            self.time_bet_label["text"] = str(timeBet)
                            if(profit-bet <= stopLost or profit >= takeProfit):
                                self.textarea.insert(
                                    END, "===> Stop win or lost" + "\n", "win")
                                break
                        else:
                            self.beting_label["text"] = "0"
                            self.textarea.insert(
                                END, str(timeRun) + ".Bet: 0.00000000 - Pass this time" + "\n")
                        self.time_run_label["text"] = str(timeRun)
                        self.textarea.see(END)
                        lineNoti = int(self.textarea.index(
                            'end-1c').split('.')[0])
                        if(lineNoti >= 100):
                            self.textarea.delete(
                                "1.0", (str(lineNoti-100+2)+".0"))
                    else:
                        time.sleep(0.3)
                    realTime = self.get_time(timeStart)
                    self.time_label["text"] = str(
                        realTime[0]) + ":" + str(realTime[1])
                except Exception as e:
                    self.textarea.insert(
                        END, "===> Stop breaking!" + "\n", "lost")
                    self.textarea.insert(END, e)
                    self.textarea.insert(END, "\n", "lost")
                    self.status_label.config(fg="red")
                    self.status_label["text"] = "Status: break"
                    self.textarea.see(END)
                    break
        except Exception as e:
            self.textarea.insert(END, "===> Stop breaking!" + "\n", "lost")
            self.textarea.insert(END, e)
            self.textarea.insert(END, "\n", "lost")
            self.status_label.config(fg="red")
            self.status_label["text"] = "Status: fail"
            self.textarea.see(END)

    def run(self):
        self.t = threading.Thread(target=self.rule).start()


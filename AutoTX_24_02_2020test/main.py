from tkinter import Tk, RIGHT, BOTH, BOTTOM, RAISED, Text, TOP, X, N, LEFT, messagebox,CENTER,NSEW
from tkinter.ttk import Frame, Button, Style, Label, Entry
import tkinter as tk
from tkinter import *
import tkinter.messagebox as mbox
import  time
from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as time_out
import random


window = tk.Tk()
window.title('AutoTX')
img = tk.Image("photo", file="icon.png")
window.iconbitmap(r'icon.ico')
window.resizable(0,0)
window.tk.call('wm','iconphoto', window._w, img)

frame1 = Frame(window, relief=RAISED, borderwidth=1)
frame1.pack(fill=X, padx=0, pady=0)  
lbl1 = Label(frame1, text="Username:", width=12)
lbl1.pack(side=LEFT, padx=0, pady=0)
entry1 = Entry(frame1, show="*")
entry1.pack(side=LEFT, padx=5, pady=0)
entry1.focus()

lbl2 = Label(frame1, text="Password:", width=9)
lbl2.pack(side=LEFT, padx=0, pady=0)
entry2 = Entry(frame1, show="*")
entry2.pack(side=LEFT, padx=5, pady=0)

frame2 = Frame(window, relief=RAISED, borderwidth=1)
frame2.pack(fill=X, padx=0, pady=0)  

lbl3 = Label(frame2, text="Money:", width=12)
lbl3.pack(side=LEFT, padx=0, pady=0)
text3 = StringVar(window, value='10000')
entry3 = Entry(frame2,textvariable=text3)
entry3.pack(side=LEFT, padx=5, pady=0)


frame3 = Frame(window, relief=RAISED, borderwidth=1)
frame3.pack(fill=X, padx=0, pady=0)

lbl12 = Label(frame3, text="Price Win", width=12)
lbl12.pack(side=LEFT, padx=0, pady=0)
text12 = StringVar(window, value='1000000')
entry12 = Entry(frame3,textvariable=text12)
entry12.pack(side=LEFT, padx=5, pady=0)

lbl14 = Label(frame3, text="Price Lose", width=9)
lbl14.pack(side=LEFT, padx=0, pady=0)
text14 = StringVar(window, value='-1000000')
entry14 = Entry(frame3,textvariable=text14)
entry14.pack(side=LEFT, padx=5, pady=0)

frame4 = Frame(window, relief=RAISED, borderwidth=1)
frame4.pack(fill=X, padx=0, pady=0)  

lbl7 = Label(frame4, text="X Lose", width=12)
lbl7.pack(side=LEFT, padx=0, pady=0)
text7 = StringVar(window, value='1')
entry7 = Entry(frame4,textvariable=text7)
entry7.pack(side=LEFT, padx=5, pady=0)

lbl9 = Label(frame4, text="Y Lose:", width=9)
lbl9.pack(side=LEFT, padx=0, pady=0)
text9 = StringVar(window, value='2')
entry9 = Entry(frame4,textvariable=text9)
entry9.pack(side=LEFT, padx=5, pady=0)

frame5 = Frame(window, relief=RAISED, borderwidth=1)
frame5.pack(fill=X, padx=0, pady=0)  

lbl15 = Label(frame5, text="X Lose 2", width=12)
lbl15.pack(side=LEFT, padx=0, pady=0)
text15 = StringVar(window, value='1')
entry15 = Entry(frame5,textvariable=text15)
entry15.pack(side=LEFT, padx=5, pady=0)

lbl16 = Label(frame5, text="Y Lose 2:", width=9)
lbl16.pack(side=LEFT, padx=0, pady=0)
text16 = StringVar(window, value='1')
entry16 = Entry(frame5,textvariable=text16)
entry16.pack(side=LEFT, padx=5, pady=0)

frame6 = Frame(window, relief=RAISED, borderwidth=1)
frame6.pack(fill=X, padx=0, pady=0)

lbl10 = Label(frame6, text="Win Streak", width=12)
lbl10.pack(side=LEFT, padx=0, pady=0)
text10 = StringVar(window, value='10')
entry10 = Entry(frame6,textvariable=text10)
entry10.pack(side=LEFT, padx=5, pady=0)

lbl11 = Label(frame6, text="Lose Streak", width=9)
lbl11.pack(side=LEFT, padx=0, pady=0)
text11 = StringVar(window, value='20')
entry11 = Entry(frame6,textvariable=text11)
entry11.pack(side=LEFT, padx=5, pady=0)

frame8 = Frame(window, relief=RAISED, borderwidth=1)
frame8.pack(fill=X, padx=0, pady=0)  

lbl4 = Label(frame8, text="Time High:", width=12)
lbl4.pack(side=LEFT, padx=0, pady=0)
text4 = StringVar(window, value='12')
entry4 = Entry(frame8,textvariable=text4)
entry4.pack(side=LEFT, padx=5, pady=0)

lbl8 = Label(frame8, text="Time Low:", width=9)
lbl8.pack(side=LEFT, padx=0, pady=0)
text8 = StringVar(window, value='4')
entry8 = Entry(frame8,textvariable=text8)
entry8.pack(side=LEFT, padx=5, pady=0)

frame9 = Frame(window, relief=RAISED, borderwidth=1)
frame9.pack(fill=X, padx=0, pady=0)  

lbl5 = Label(frame9, text="Gap Win: ", width=12)
lbl5.pack(side=LEFT, padx=0, pady=0)
text5 = StringVar(window, value='4')
entry5 = Entry(frame9,textvariable=text5)
entry5.pack(side=LEFT, padx=5, pady=0)

lbl6 = Label(frame9, text="Gap Lose: ", width=9)
lbl6.pack(side=LEFT, padx=0, pady=0)
text6 = StringVar(window, value='4')
entry6 = Entry(frame9,textvariable=text6)
entry6.pack(side=LEFT, padx=5, pady=0)

frame10 = Frame(window, relief=RAISED, borderwidth=1)
frame10.pack(fill=X, padx=0, pady=0)  

lbl18 = Label(frame10, text="Reload sau Win: ", width=12)
lbl18.pack(side=LEFT, padx=0, pady=0)
text18 = StringVar(window, value='25')
entry18 = Entry(frame10,textvariable=text18)
entry18.pack(side=LEFT, padx=5, pady=0)

frame12 = Frame(window, relief=RAISED, borderwidth=0)
frame12.pack(fill=X, padx=0, pady=0)  
frame11 = Frame(window, relief=RAISED, borderwidth=0)
frame11.pack(fill=X, padx=0, pady=0)  


lbl19 = Label(frame11, text="Win: 0", width=11)
lbl19.pack(side=LEFT, padx=0, pady=0)
lbl20 = Label(frame11, text="Lose: 0", width=11)
lbl20.pack(side=LEFT, padx=0, pady=0)
lbl21 = Label(frame11, text="Tien bet: 0", width=11)
lbl21.pack(side=LEFT, padx=0, pady=0)
lbl22 = Label(frame11, text="Lai: 0", width=11)
lbl22.pack(side=LEFT, padx=0, pady=0)
lbl23 = Label(frame11, text="Gap Win: 0", width=15)
lbl23.pack(side=LEFT, padx=0, pady=0)
lbl24 = Label(frame11, text="Status: relaxing", width=12)
lbl24.pack(side=LEFT, padx=0, pady=0)
lbl25 = Label(frame12, text="Start: 0", width=15)
lbl25.pack(side=LEFT, padx=0, pady=0)
lbl26 = Label(frame12, text="New: 0", width=15)
lbl26.pack(side=LEFT, padx=0, pady=0)
lbl27 = Label(frame12, text="Day tien dai: 0", width=20)
lbl27.pack(side=LEFT, padx=0, pady=0)
lbl28 = Label(frame12, text="Bet max: 0", width=15)
lbl28.pack(side=LEFT, padx=0, pady=0)
#frame12 = Frame(window, relief=RAISED, borderwidth=0)
#frame12.pack(fill=X, padx=0, pady=0)  
#txt = Text(frame1,heigh=6,width=48)
#txt.pack(fill=BOTH, pady=0, padx=5)

def get_data():
    xTime_main = entry7.get()
    xTime = entry7.get()
    xTime2 = entry15.get()
    xTime2_main=xTime2
    yTime2 = entry16.get()
    yTime_main = entry9.get()
    yTime = entry9.get()
    reload_time=entry18.get()
    money_main=entry3.get()
    money_main_bet = money_main
    money = money_main
    money_win=entry12.get()
    money_lose=entry14.get()
    time=entry4.get()
    time_low=entry8.get()    
    gapWinLose=entry5.get()
    gapLoseWin=entry6.get()
    win_streak_main=entry10.get()
    win_streak=0
    win_streak_alltime=0
    lose_streak_main=entry11.get()
    lose_streak=0
    lose_streak_alltime=0
    money_start = driver.find_element_by_id('goldLabel').get_attribute("textContent").replace(".","")
    money_new = float(money_start)
    time_win = 0
    time_win_reload=0
    time_win_betting = 0
    time_lose = 0
    time_lose_betting = 0
    stop=False
    a=int(money_main)
    b=int(money_start)
    c=int(yTime_main)
    e=0
    g=0
    countt=0
    cBx1dt=var1.get()
    cBx2dt=var2.get()
    if cBx1dt == cBx2dt:
        mbox.showerror("Thong bao", "Nhap du lieu ben danh")
    while e<b:
        if g<=6:
            countt+=1
            g+=1
            e+=a
        if g>=6:
            g=0
            a=a*c
        if e<b:
            maxA=a
    with open('data.md','w+') as data:
        data.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
            xTime_main,xTime,xTime2,xTime2_main,yTime2,yTime_main,yTime,reload_time,money_main,money_main_bet,money,money_win,money_lose,time,time_low,gapWinLose,gapLoseWin,win_streak_main,win_streak,win_streak_alltime,lose_streak_main,lose_streak,lose_streak_alltime,money_start,money_new,time_win,time_win_reload,time_win_betting,time_lose,time_lose_betting,stop,countt,maxA,cBx1dt,cBx2dt
        ))
    with open('time.md','w+') as tmd:
        tmd.write('null')
    mbox.showerror("Thong bao", "Lay du lieu thanh cong")

def web():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get('http://fan79.vip/#games')

def stop_bet():
    try:
        driver.close()
        mbox.showerror("Thong bao", "Tat cua so thanh cong")
    except:
        mbox.showerror("Thong bao", "Khong co du lieu")

def clicked():
    data2=entry2.get()
    data1=entry1.get()

    sleep(1) 
    username_box = driver.find_element_by_id('txtUserName') 
    username_box.send_keys(data1) 
    password_box = driver.find_element_by_id('txtPass') 
    password_box.send_keys(data2) 
    btnlogin = driver.find_element_by_id('btnlogin')
    driver.execute_script("arguments[0].click();", btnlogin)
    mbox.showerror("Thong bao", "Tat trinh duyet truoc khi tat ung dung")
    #login_box = driver.find_element_by_id('btnlogin') 
    #topics_xpath = "//span[@class='btn-login' and @id='btnlogin']"
    #driver.find_element_by_xpath(topics_xpath).click()
    #sleep(1)
def bet():
    time_get = driver.find_element_by_id('time').get_attribute("textContent")
    with open('data.md') as data:
        count=1
        for line in data:
            if count==1:
                xTime_main = int('{}'.format(line.strip()))
            if count==2:
                xTime = int('{}'.format(line.strip()))
            if count==3:
                xTime2 = int('{}'.format(line.strip()))
            if count==4:
                xTime2_main= int('{}'.format(line.strip()))
            if count==5:
                yTime2 = int('{}'.format(line.strip()))
            if count==6:
                yTime_main = int('{}'.format(line.strip()))
            if count==7:
                yTime = int('{}'.format(line.strip()))
            if count==8:
                reload_time= int('{}'.format(line.strip()))
            if count==9:
                money_main= int('{}'.format(line.strip()))
            if count==10:
                money_main_bet = int('{}'.format(line.strip()))
            if count==11:
                money = int('{}'.format(line.strip()))
            if count==12:
                money_win= int('{}'.format(line.strip()))
            if count==13:
                money_lose= int('{}'.format(line.strip()))
            if count==14:
                time= int('{}'.format(line.strip()))
            if count==15:
                time_low= int('{}'.format(line.strip()))
            if count==16:
                gapWinLose= int('{}'.format(line.strip()))
            if count==17:
                gapLoseWin= int('{}'.format(line.strip()))
            if count==18:
                win_streak_main= int('{}'.format(line.strip()))
            if count==19:
                win_streak= int('{}'.format(line.strip()))
            if count==20:
                win_streak_alltime= int('{}'.format(line.strip()))
            if count==21:
                lose_streak_main= int('{}'.format(line.strip()))
            if count==22:
                lose_streak= int('{}'.format(line.strip()))
            if count==23:
                lose_streak_alltime= int('{}'.format(line.strip()))
            if count==24:
                money_start = int('{}'.format(line.strip()))
            if count==25:
                money_new = float('{}'.format(line.strip()))
            if count==26:
                time_win = int('{}'.format(line.strip()))
            if count==27:
                time_win_reload= int('{}'.format(line.strip()))
            if count==28:
                time_win_betting = int('{}'.format(line.strip()))
            if count==29:
                time_lose = int('{}'.format(line.strip()))
            if count==30:
                time_lose_betting = int('{}'.format(line.strip()))
            if count==31:
                stop= '{}'.format(line.strip())
            if count==32:
                countt= '{}'.format(line.strip())
            if count==33:
                maxA= '{}'.format(line.strip())
            if count==34:
                cBx1dt = int('{}'.format(line.strip()))
            if count==35:
                cBx2dt = int('{}'.format(line.strip()))
            count+=1
    time_sleep = 60
    dataBet = open('autotaixiu.md' , 'a')
    with open('time.md') as tbm:
        time_bet = tbm.read()

    if time_get == "00:59" or time_get == "00:58" or time_get == "00:57":
        time_random=random.randrange(int(time_low),int(time))
        time_bet = ("00:%s" %(60 - int(time_random)))
        with open('time.md' , 'w+') as tb:
            tb.write(time_bet)
    print('%s-%s'%(time_bet,time_get))
    if str(time_get) == str(time_bet):
        numberPriceHigh = driver.find_element_by_id('totalbetOver').get_attribute("textContent").replace(".","")
        numberPriceLow = driver.find_element_by_id('totalbetUnder').get_attribute("textContent").replace(".","")
        roleBet = driver.find_element_by_id('sessionid').get_attribute("textContent")
        #print("Tai: %s -- Xiu: %s" %(numberPriceHigh,numberPriceLow ))
        if int(numberPriceHigh) > int(numberPriceLow) :
            bet_Tai = driver.find_element_by_id('txtbetpersonOver')
            bet_Tai.send_keys(str(money) + "\n")
            #print("%s-%s-Bet Tai : %s"%(roleBet,time_bet,money))      
            #sleep(time_sleep)
            try:
                WebDriverWait(driver, time_sleep).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.location.tai.active")))                    
                if cBx1dt==1:
                #resultBetTai = driver.find_element_by_css_selector('div.location.tai.active')
                    money_new += (float(money)*98/100)
                    profit = int(float(money_new)-float(money_start))
                    time_win +=1
                    time_win_reload+=1
                    time_win_betting+=1
                    win_streak_alltime+=1
                    lose_streak=0
                    lose_streak_alltime=0
                    money = money_main_bet
                    #print("Win--Profit: ",profit)
                    #print("Win: %s -- Lose: %s" %(time_win,time_lose))
                    dataBet = open('autotaixiu.md' , 'a')
                    data_tai_win=("%s-%s-Bet Tai : %s\nWin: %s Streak--Profit: %s\nWin: %s -- Lose: %s\n\n"%(roleBet,time_bet,money,win_streak_alltime,profit,time_win,time_lose))
                    dataBet.write(data_tai_win)
                    if  time_win_betting - time_lose_betting >=(int(gapWinLose)):
                        time_lose_betting = 0
                        time_win_betting = 0
                        xTime=xTime_main
                        xTime2=xTime2_main
                        money_main_bet = money_main
                        money=money_main_bet
                        #print("Chenh win %s van bet tro lai: %s" %(gapWinLose,money))
                    if profit >= int(money_win):
                        #print("Chốt lời")
                        #print("-----------------")
                        stop=True
                    if int(time_win_reload)>=int(reload_time):
                        time_win_reload=0                        
                        driver.refresh()
                        #print("Reload success!")
                        sleep(10)
                    #print("-----------------")
                if cBx2dt==1:
                    money_new -= (float(money))
                    profit = int(float(money_new)-float(money_start))
                    time_lose +=1
                    time_lose_betting+=1
                    lose_streak+=1
                    lose_streak_alltime+=1
                    win_streak_alltime=0
                    money = int(money)*int(xTime)+int(money*5/100)
                    #print("Lose--Profit: ",profit)
                    #print("Win: %s -- Lose: %s" %(time_win,time_lose))
                    dataBet = open('autotaixiu.md' , 'a')
                    data_tai_lose = ("%s-%s-Bet Tai : %s\nLose: %s Streak--Profit: %s\nWin: %s -- Lose: %s\n\n"%(roleBet,time_bet,money,lose_streak_alltime,profit,time_win,time_lose))
                    dataBet.write(data_tai_lose)
                    if int(lose_streak) >= int(lose_streak_main):
                        lose_streak=0
                        money_main_bet=int(money_main_bet)*int(xTime2)
                        money=money_main_bet
                    if  time_lose_betting - time_win_betting >=(int(gapLoseWin)):
                        time_lose_betting = 0
                        time_win_betting = 0
                        xTime =1
                        xTime2=1
                        money_main_bet = int(money_main_bet)*int(yTime)+int(money*5/100)
                        money=money_main_bet
                        #print("Tang gia tri bet len khi chenh thua %s van: %s" %(gapLoseWin,money))                    
                if profit<=int(money_lose):
                    #print("Chốt lỗ")
                    #print("-----------------")
                    stop=True
                #print("-----------------")
            except time_out:
                if cBx1dt==1:
                    money_new -= (float(money))
                    profit = int(float(money_new)-float(money_start))
                    time_lose +=1
                    time_lose_betting+=1
                    lose_streak+=1
                    lose_streak_alltime+=1
                    win_streak_alltime=0
                    money = int(money)*int(xTime)+int(money*5/100)
                    #print("Lose--Profit: ",profit)
                    #print("Win: %s -- Lose: %s" %(time_win,time_lose))
                    dataBet = open('autotaixiu.md' , 'a')
                    data_tai_lose = ("%s-%s-Bet Tai : %s\nLose: %s Streak--Profit: %s\nWin: %s -- Lose: %s\n\n"%(roleBet,time_bet,money,lose_streak_alltime,profit,time_win,time_lose))
                    dataBet.write(data_tai_lose)
                    if int(lose_streak) >= int(lose_streak_main):
                        lose_streak=0
                        money_main_bet=int(money_main_bet)*int(xTime2)
                        money=money_main_bet
                    if  time_lose_betting - time_win_betting >=(int(gapLoseWin)):
                        time_lose_betting = 0
                        time_win_betting = 0
                        xTime =1
                        xTime2=1
                        money_main_bet = int(money_main_bet)*int(yTime)+int(money*5/100)
                        money=money_main_bet
                        #print("Tang gia tri bet len khi chenh thua %s van: %s" %(gapLoseWin,money))                    
                    if profit<=int(money_lose):
                        #print("Chốt lỗ")
                        #print("-----------------")
                        stop=True
                    #print("-----------------")
                if cBx2dt==1:
                    money_new += (float(money)*98/100)
                    profit = int(float(money_new)-float(money_start))
                    time_win +=1
                    time_win_reload+=1
                    time_win_betting+=1
                    win_streak_alltime+=1
                    lose_streak=0
                    lose_streak_alltime=0
                    money = money_main_bet
                    #print("Win--Profit: ",profit)
                    #print("Win: %s -- Lose: %s" %(time_win,time_lose))
                    dataBet = open('autotaixiu.md' , 'a')
                    data_tai_win=("%s-%s-Bet Tai : %s\nWin: %s Streak--Profit: %s\nWin: %s -- Lose: %s\n\n"%(roleBet,time_bet,money,win_streak_alltime,profit,time_win,time_lose))
                    dataBet.write(data_tai_win)
                    if  time_win_betting - time_lose_betting >=(int(gapWinLose)):
                        time_lose_betting = 0
                        time_win_betting = 0
                        xTime=xTime_main
                        xTime2=xTime2_main
                        money_main_bet = money_main
                        money=money_main_bet
                        #print("Chenh win %s van bet tro lai: %s" %(gapWinLose,money))
                    if profit >= int(money_win):
                        #print("Chốt lời")
                        #print("-----------------")
                        stop=True
                    if int(time_win_reload)>=int(reload_time):
                        time_win_reload=0                        
                        driver.refresh()
                        #print("Reload success!")
                        sleep(10)
                    #print("-----------------")
        if int(numberPriceHigh) < int(numberPriceLow) :
            bet_Tai = driver.find_element_by_id('txtbetpersonUnder')
            bet_Tai.send_keys(str(money) + "\n")
            #print("%s-%s-Bet Xiu : %s"%(roleBet,time_bet,money))             
            #sleep(time_sleep)
            try:
                WebDriverWait(driver, time_sleep).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.location.xiu.active")))
                if cBx1dt==1:
                #resultBetXiu = driver.find_element_by_css_selector('div.location.xiu.active')                    
                    time_win +=1
                    time_win_reload+=1
                    time_win_betting+=1
                    win_streak_alltime+=1
                    lose_streak=0
                    lose_streak_alltime=0
                    money_new += (float(money)*98/100)
                    profit = int(float(money_new)-float(money_start))
                    money = money_main_bet
                    #print("Win--Profit: ",profit)
                    #print("Win: %s -- Lose: %s" %(time_win,time_lose))
                    dataBet = open('autotaixiu.md' , 'a')
                    data_xiu_win=("%s-%s-Bet Xiu : %s\nWin: %s Streak--Profit: %s\nWin: %s -- Lose: %s\n\n"%(roleBet,time_bet,money,win_streak_alltime,profit,time_win,time_lose))
                    dataBet.write(data_xiu_win)
                    if  time_win_betting - time_lose_betting >=(int(gapWinLose)):
                        time_lose_betting = 0
                        time_win_betting = 0
                        xTime=xTime_main
                        xTime2=xTime2_main
                        money_main_bet = money_main
                        money=money_main_bet
                        #print("Chenh win %s van bet tro lai: %s" %(gapWinLose,money))                        
                    if profit >= int(money_win):
                        #print("Chốt lời")
                        #print("-----------------")
                        stop=True
                    if int(time_win_reload)>=int(reload_time):
                        time_win_reload=0
                        driver.refresh()
                        #print("Reload success!")
                        sleep(10)
                    #print("-----------------")
                if cBx2dt==1:
                    money_new -= (float(money))
                    profit = int(float(money_new)-float(money_start))
                    time_lose +=1                    
                    time_lose_betting+=1
                    lose_streak+=1
                    lose_streak_alltime+=1
                    win_streak_alltime=0
                    money = int(money)*int(xTime)+int(money*5/100)
                    if int(lose_streak) >= int(lose_streak_main):
                        lose_streak=0
                        money_main_bet=int(money_main_bet)*int(xTime2)
                        money=money_main_bet
                    #print("Lose--Profit: ",profit)
                    #print("Win: %s -- Lose: %s" %(time_win,time_lose))
                    dataBet = open('autotaixiu.md' , 'a')
                    data_xiu_lose = ("%s-%s-Bet Xiu : %s\nLose: %s Streak--Profit: %s\nWin: %s -- Lose: %s\n\n"%(roleBet,time_bet,money,lose_streak_alltime,profit,time_win,time_lose))
                    dataBet.write(data_xiu_lose)
                    if  time_lose_betting - time_win_betting >=(int(gapLoseWin)):
                        time_lose_betting = 0
                        time_win_betting = 0
                        xTime =1
                        xTime2=1
                        money_main_bet = int(money_main_bet)*int(yTime)+int(money*5/100)
                        money=money_main_bet
                        #print("Tang gia tri bet len khi chenh thua %s van: %s" %(gapLoseWin,money))            
                    if profit<=int(money_lose):
                        #print("Chốt lỗ")
                        #print("-----------------")
                        stop=True
                    #print("-----------------")
            except time_out:
                if cBx1dt==1:
                    money_new -= (float(money))
                    profit = int(float(money_new)-float(money_start))
                    time_lose +=1                    
                    time_lose_betting+=1
                    lose_streak+=1
                    lose_streak_alltime+=1
                    win_streak_alltime=0
                    money = int(money)*int(xTime)+int(money*5/100)
                    if int(lose_streak) >= int(lose_streak_main):
                        lose_streak=0
                        money_main_bet=int(money_main_bet)*int(xTime2)
                        money=money_main_bet
                    #print("Lose--Profit: ",profit)
                    #print("Win: %s -- Lose: %s" %(time_win,time_lose))
                    dataBet = open('autotaixiu.md' , 'a')
                    data_xiu_lose = ("%s-%s-Bet Xiu : %s\nLose: %s Streak--Profit: %s\nWin: %s -- Lose: %s\n\n"%(roleBet,time_bet,money,lose_streak_alltime,profit,time_win,time_lose))
                    dataBet.write(data_xiu_lose)
                    if  time_lose_betting - time_win_betting >=(int(gapLoseWin)):
                        time_lose_betting = 0
                        time_win_betting = 0
                        xTime =1
                        xTime2=1
                        money_main_bet = int(money_main_bet)*int(yTime)+int(money*5/100)
                        money=money_main_bet
                        #print("Tang gia tri bet len khi chenh thua %s van: %s" %(gapLoseWin,money))            
                    if profit<=int(money_lose):
                        #print("Chốt lỗ")
                        #print("-----------------")
                        stop=True
                    #print("-----------------")
                if cBx2dt==1:
                    time_win +=1
                    time_win_reload+=1
                    time_win_betting+=1
                    win_streak_alltime+=1
                    lose_streak=0
                    lose_streak_alltime=0
                    money_new += (float(money)*98/100)
                    profit = int(float(money_new)-float(money_start))
                    money = money_main_bet
                    #print("Win--Profit: ",profit)
                    #print("Win: %s -- Lose: %s" %(time_win,time_lose))
                    dataBet = open('autotaixiu.md' , 'a')
                    data_xiu_win=("%s-%s-Bet Xiu : %s\nWin: %s Streak--Profit: %s\nWin: %s -- Lose: %s\n\n"%(roleBet,time_bet,money,win_streak_alltime,profit,time_win,time_lose))
                    dataBet.write(data_xiu_win)
                    if  time_win_betting - time_lose_betting >=(int(gapWinLose)):
                        time_lose_betting = 0
                        time_win_betting = 0
                        xTime=xTime_main
                        xTime2=xTime2_main
                        money_main_bet = money_main
                        money=money_main_bet
                        #print("Chenh win %s van bet tro lai: %s" %(gapWinLose,money))                        
                    if profit >= int(money_win):
                        #print("Chốt lời")
                        #print("-----------------")
                        stop=True
                    if int(time_win_reload)>=int(reload_time):
                        time_win_reload=0
                        driver.refresh()
                        #print("Reload success!")
                        sleep(10)
                    #print("-----------------")
        with open('data.md','w+') as data:
            data.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
                xTime_main,xTime,xTime2,xTime2_main,yTime2,yTime_main,yTime,reload_time,money_main,money_main_bet,money,money_win,money_lose,time,time_low,gapWinLose,gapLoseWin,win_streak_main,win_streak,win_streak_alltime,lose_streak_main,lose_streak,lose_streak_alltime,money_start,money_new,time_win,time_win_reload,time_win_betting,time_lose,time_lose_betting,stop,count,maxA,cBx1dt,cBx2dt
            ))
        lbl22['text']='Lai: %s'%(profit)
    if stop !=True:
        lbl19['text']='Win: %s'%(time_win)
        lbl20['text']='Lose: %s'%(time_lose)
        lbl21['text']='Bet: %s'%(money)
        lbl23['text']='Gap Win: %s'%(time_win_betting-time_lose_betting)
        lbl24['text']='Status: betting'
        lbl25['text']='Start: %s'%(money_start)
        lbl26['text']='New: %s'%(money_new)
        lbl27['text']='Day tien dai: %s'%(countt)
        lbl28['text']='Bet max: %s'%(maxA)
        window.after(1000,bet)
    if stop ==True:
        lbl24['text']='Status: relaxing'

def quitSoft():    
    window.quit()

def scrs():
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('screenshot.png')

webButton = Button(frame1, text="Web", command=web)
webButton.pack(side=RIGHT) 
loginButton = Button(frame1, text="Login", command=clicked)
loginButton.pack(side=RIGHT) 
scrButton = Button(frame3, text="Screenshot", command=scrs)
scrButton.pack(side=RIGHT)
frame11 = Frame(window, relief=RAISED, borderwidth=1)
frame11.pack(fill=X, padx=0, pady=0)  

frame11 = Frame(window, relief=RAISED, borderwidth=1)
frame11.pack(fill=X, padx=0, pady=0)  
closeButton = Button(frame11, text="Get data", command=get_data)
closeButton.pack(side=RIGHT)
betButton = Button(frame11, text="Bet", command=bet)
betButton.pack(side=RIGHT)
closeButton = Button(frame11, text="Close Chrome", command=stop_bet)
closeButton.pack(side=RIGHT)
var1 = IntVar()
cBx1= Checkbutton(frame2, text="Nhiều hơn", variable=var1)
cBx1.pack(side=LEFT, padx=5, pady=0)
var2 = IntVar()
cBx2= Checkbutton(frame2, text="Ít hơn", variable=var2)
cBx2.pack(side=LEFT, padx=5, pady=0)

#window.after(1000,bet)
window.mainloop()

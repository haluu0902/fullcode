import tkinter as tk
from tkinter import *
import threading
from sendMess import send
import play

def run_ui():
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

    login_button = Button(frame1, text="Login", command=login)
    login_button.pack(side=RIGHT, padx=5, pady=0) 
    start_button = Button(frame_final, text="Start Bet", command=run)
    start_button.pack(side=RIGHT, padx=5, pady=5) 
    send_message_button = Button(frame_final, text="Send Message to Discord", command=run_send_message)
    send_message_button.pack(side=RIGHT, padx=5, pady=5) 
    root.mainloop()
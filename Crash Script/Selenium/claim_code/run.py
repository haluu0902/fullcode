import tkinter as tk
from tkinter import *
import control_chrome
from threading import Thread

root = tk.Tk()
root.title("Auto Shitcode BC.Game - By: SaviorXXI")
img = tk.Image("photo", file="./images/icon.png")
root.iconbitmap(r'./images/icon.ico')
root.resizable(0,0)
root.tk.call('wm','iconphoto', root._w, img)

frame1 = Frame(root, relief=RAISED, borderwidth=1)
frame1.pack(fill=X, padx=0, pady=0)

code_label = Label(frame1, text="Code:", width=18)
code_label.pack(side=LEFT, padx=0, pady=0)
code_value = StringVar(root, value='$[BCGAME-1AECB5RAQCFSKUXGPBKWJSPKQ9TJRA1ILH]$')
input_code = Entry(frame1,textvariable=code_value, width=55)
input_code.pack(side=LEFT, padx=5, pady=0)

frame2 = Frame(root, relief=RAISED, borderwidth=1)
frame2.pack(fill=X, padx=0, pady=0)

number_browser_label = Label(frame2, text="Number of account:", width=18)
number_browser_label.pack(side=LEFT, padx=0, pady=0)
number_browser_value = StringVar(root, value='20')
input_number_browser = Entry(frame2,textvariable=number_browser_value, width=55)
input_number_browser.pack(side=LEFT, padx=5, pady=0)

def OpenBrowser():
    global runF
    runF = control_chrome.ControllChrome(int(input_number_browser.get()))
    runF.open_browser()
def Claim():
    runF.send_code_thread(input_code.get())


frameButton = Frame(root, relief=RAISED, borderwidth=1)
frameButton.pack(fill=X, padx=0, pady=0)
start_button = Button(frameButton, text="Start Claim", command=Claim)
start_button.pack(side=RIGHT, padx=5, pady=0) 
open_button = Button(frameButton, text="Open Browser", command=OpenBrowser)
open_button.pack(side=RIGHT, padx=5, pady=5) 
root.mainloop()

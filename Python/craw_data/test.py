from selenium import webdriver
import selenium
import time
import json
data=[]
with open(r'data.json', 'r', encoding='utf-8') as dt:
    data = json.load(dt)
print(len(data))
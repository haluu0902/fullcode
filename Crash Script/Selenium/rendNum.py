import random
import time
import math
lastPayout=0
payouting = 2
bet = 10
bet1 = 10
bet2 = 10
bet3 = 10
bet4 = 10
maxBet = 10
profit = 0.00                             
while True:    
    payout = random.choice(range(10,1000))/10
    f = open("./data/history_1.txt", "a+")
    f.write(str(payout))
    f.write("-")
    f.close()
    print (payout)
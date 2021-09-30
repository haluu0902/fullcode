from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
from threading import Thread
import matplotlib.ticker as mticker
import time
from math import floor


class LiveGraph:
    def __init__(self):
        self.x_data, self.y_data = [], []
        self.figure = plt.figure()

        self.line, = plt.plot(self.x_data, self.y_data)
        self.animation = FuncAnimation(self.figure, self.update, interval=1000)
        self.th = Thread(target=self.thread_f, daemon=True)
        self.th.start()
    def re_place_step(self):
        if(len(self.y_data)<=10):
            return 1
        else:
            return floor(len(self.y_data)/10)
    def update(self, frame):
        self.line.set_data(self.x_data, self.y_data)
        self.figure.gca().xaxis.set_major_locator(mticker.MultipleLocator(self.re_place_step()))
        self.figure.gca().relim()
        self.figure.gca().autoscale_view()
        
        return self.line,

    def show(self):
        plt.show()

    def thread_f(self):
        x = 0
        count=0
        while True:
            self.x_data.append(x)
            x += 1
            count+=1
            self.y_data.append(count)   
            time.sleep(1)  

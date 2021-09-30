from tkinter import * 
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.ticker as mticker
y = [0,2,1,6]
x = [0,1,2,3]   
# plot function is created for 
# plotting the graph in 
# tkinter window
def plot():
  
    # the figure that will contain the plot
    fig = plt.figure()
    line = plt.plot(x, y)
    line.set_data(x, y)
    # adding the subplot
    plot1 = fig.add_subplot(111)
    y.append(input_bet.get())
    # plotting the graph
    plot1.plot(y)
  

    # list of squares
    fig.gca().relim()
    fig.gca().autoscale_view()
    fig.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
  
# the main Tkinter window
window = Tk()
  
# setting the title 
window.title('Plotting in Tkinter')
  
# dimensions of the main window
window.geometry("500x500")
input_bet = Entry(window,textvariable=1)
input_bet.pack(side=LEFT, padx=5, pady=0)  
# button that displays the plot
plot_button = Button(master = window, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Plot")
  
# place the button 
# in main window
plot_button.pack()
  
# run the gui
window.mainloop()
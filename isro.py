from itertools import groupby
from re import A
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
i=0
fig, ax = plt.subplots()

global a
ax.plot(0*x, 0 * x + x, picker=5, label="a")
ax.plot(1*x, 1 * x + x, picker=5, label="b")
ax.plot(2*x, x + x, picker=5, label="c")
ax.plot(x*x, 0 * x + x, picker=5, label="d")
ax.plot(x + x, picker=5, label="e")
ax.plot(x, picker=5, label="f")
ax.plot(x, 0 * x + x, picker=5, label="g") 

a=[]      

def on_pick(event):
    
 
    # print (event.artist.get_label(),"clicked")
    # event.artist.set_visible(not event.artist.get_visible())    (for making selected lines invisible)
    event.artist.set_color("grey") #for greying out the selected lines
    event.artist.set_picker(False) #cannot be selected again
    fig.canvas.draw()
def add_evt(event):
    a.append(event.artist.get_label())
    # print(a)
    
def groupbylist(event): 
    global i 
    i=i+1
    print ("group",i,"->",a)
    
    a.clear()
fig.canvas.callbacks.connect('pick_event', on_pick)
fig.canvas.callbacks.connect('pick_event',add_evt)
fig.canvas.callbacks.connect('button_release_event',groupbylist)
    



plt.show()
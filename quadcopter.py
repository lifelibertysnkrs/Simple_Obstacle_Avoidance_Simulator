from map import *


class quadcopter():
    def __init__(self, canvas, x , y):
        canvas.create_text(x, y, text="X", anchor=CENTER, fill="green", font="Times 22") #Creates x at quadcopter position
    def delete(self, canvas, x , y):   
        canvas.create_rectangle(x-25,y-25,x+25, y+25, fill = "black") #Creates x at quadcopter position
    

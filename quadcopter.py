from map import *


class quadcopter():
    def __init__(self, canvas, x , y):
        canvas.create_text(x, y, text="X", anchor=SW, fill="green", font="Times 22") #Creates x at quadcopter position
        

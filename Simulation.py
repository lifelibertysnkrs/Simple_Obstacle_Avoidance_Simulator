from map import *
from quadcopter import *




class Simulation():
    def __init__(self, startx, starty, targetx, targety, difficulty):
        self.x = startx
        self.y = starty
        self.deltax = 0
        self.deltay = 0
        self.board = map([[startx+self.deltax, starty+self.deltay], [startx-30+self.deltax,starty-30+self.deltay],[startx+30+self.deltax,starty-30+self.deltay], [startx-30+self.deltax,starty+30+self.deltay], [startx+30+self.deltax,starty+30+self.deltay]], [targetx,targety], difficulty)
        self.canvas = self.board.canvas 
        self.board.obstacles()
        self.board.target()
        self.canvas.bind("<1>", self.focus)   #user must click in window before key inputs can be made
        self.canvas.bind("<Up>", self.forward) #key inputs
        self.canvas.bind("<Down>", self.backward)
        self.canvas.bind("<Left>", self.left)
        self.canvas.bind("<Right>", self.right)
          
        

    def check(self): #checks for collisions or if quadcopter has reached target then passes on to movement
        if self.board.collision():
            self.board.canvas.create_text(100, 100, text="COLLISION", anchor=SW, fill="green", font="Times 22")           
        if self.board.targetReached():
            self.board.canvas.create_text(100, 150, text="SUCCESS!", anchor=SW, fill="green", font="Times 22")
        print self.board.sensordata()
        self.movement(self.deltax,self.deltay)

    def movement(self, deltax, deltay): #moves quadcopter around
        
        self.x+= deltax
        self.y += deltay
    
        for point in self.board.quadcopter:
            point[0]+=deltax
            point[1]+=deltay
        self.deltax = 0
        self.deltay = 0
        

        self.quad = quadcopter(self.canvas, self.x, self.y)
        self.board.root.after(10, self.check)

    def render(self):
        self.board.root.after(10, self.check)    
        self.board.root.mainloop()
        
    def forward(self, event):
        self.deltay = -10
        quaddel = self.quad.delete(self.canvas, self.x, self.y)
    def backward(self, event):
        self.deltay = 10
        quaddel = self.quad.delete(self.canvas, self.x, self.y)
    def left(self, event):
        self.deltax = -10
        quaddel = self.quad.delete(self.canvas, self.x, self.y)
    def right(self, event):
        self.deltax = 10
        quaddel = self.quad.delete(self.canvas, self.x, self.y)
    def focus(self, event):
        self.canvas.focus_set()
        quaddel = self.quad.delete(self.canvas, self.x, self.y)


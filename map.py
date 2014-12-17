from Tkinter import *
import random
class map():
    def __init__(self, quad, target, difficulty):
        self.root = root = Tk()
        self.quadcopter = quad
        canvas = Canvas(root, width=900, height=600)
        canvas.pack()
        canvas.create_rectangle(  0,   0, 900, 600, fill="black") #background
        self.canvas = canvas
        self.quadcopter = quad
        self.targetx = target[0]
        self.targety = target[1]
        self.difficulty = difficulty #number of obstacles



    def obstacles(self):
        obstacles = []
        difficulty = self.difficulty
        while difficulty > 0:
            x = self.targetx #set obstacle in target
            y = self.targety 
            while ((x > self.targetx-120) and (x < self.targetx+60)) and (y > self.targety-70 and y < self.targety+70): #keep choosing new points for obstacle untill it is no longer in target
                x = random.randint(0,800)
            
                y = random.randint(0,550)
            obstacles.append([x, y, (x+60), (y+3)])
            difficulty -=1
        for obstacle in obstacles:
            
            self.canvas.create_rectangle(obstacle, fill = "red")
        self.obstaclelist = obstacles
        

    def collision(self): #detects if quadcopter has hit obstacle
        for obstacle in self.obstaclelist:
            for point in self.quadcopter: #quadcopter is defined by 5 points: center and each corner
                if (point[0]+5 >= (obstacle[0]) and point[0]-5 <= (obstacle[2])) and (point[1]+5 >= (obstacle[1]) and (point[1]-5 <= (obstacle[3]))):
                    return True
                
    def sensordata(self):
         for obstacle in self.obstaclelist:
            for point in self.quadcopter: #quadcopter is defined by 5 points: center and each corner
                if (point[0]+5 >= (obstacle[0]) and point[0]-5 <= (obstacle[2])) and (point[1]+25 >= (obstacle[1]) and (point[1] <= (obstacle[3]))):
                    return "Down"
            for point in self.quadcopter: #quadcopter is defined by 5 points: center and each corner
                if (point[0]+5 >= (obstacle[0]) and point[0]-5 <= (obstacle[2])) and (point[1] >= (obstacle[1]) and (point[1]-25 <= (obstacle[3]))):
                    return "Up"
            for point in self.quadcopter: #quadcopter is defined by 5 points: center and each corner
                if (point[0]+55 >= (obstacle[0]) and point[0] <= (obstacle[2])) and (point[1]+5 >= (obstacle[1]) and (point[1]-5 <= (obstacle[3]))):
                    return "Right"
            for point in self.quadcopter: #quadcopter is defined by 5 points: center and each corner
                if (point[0] >= (obstacle[0]) and point[0]-55 <= (obstacle[2])) and (point[1]+5 >= (obstacle[1]) and (point[1]-5 <= (obstacle[3]))):
                    return "Left"    
            

    def target(self):
        x = self.targetx
        y = self.targety
        self.canvas.create_rectangle(x-55,y-55,x+55, y+55, fill = "blue")
        self.canvas.create_rectangle(x-50,y-50,x+50, y+50, fill = "white")
        self.canvas.create_text(x, y-10, text="TARGET", fill="red", font="Helvetica 10 bold underline")
        self.canvas.create_text(x, y+10, text=("(", str(x), ",", str(y), ")"), fill="red", font="Helvetica 10")
        self.targetspace = [x-50,y-50,x+50, y+50]
        return self.targetspace

    def targetReached(self): #detects if quadcopter has reached objective
        for point in self.quadcopter:
            if (point[0]-10 >= self.targetspace[0] and point[0]+10 <= self.targetspace[2]) and (point[1]-10 >= self.targetspace[1] and point[1]+10 <= self.targetspace[3]):
                return True














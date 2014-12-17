from Simulation import *
default = raw_input("Welcome. \n To use default settings, press y, else, press any other key" )
if default == 'y':
    print "Running simulator with default settings"
    run = Simulation(500,500,400,400,2)
else:
    x = raw_input("Enter quadcopter start x coordinate: ")
    y = raw_input("Enter quadcopter start y coordinate: ")
    tx = raw_input("Enter target x coordinate: ")
    ty = raw_input("Enter target y coordinate: ")
    difficulty = raw_input("Enter number of obstacles: ")
    run = Simulation(int(x),int(y),int(tx),int(ty),int(difficulty))

run.render()



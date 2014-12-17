Simple Obstacle Avoidance Simulator
===================================

A simulator for quadcopter obstacle avoidance

If you want to run the program using your arrow keys and minimal set up, run simplerun.py.

The program can also be used by an obstacle avoidance algorithm running from either another python program or a c++ program.

Run simulation by importing Simulation.py calling Simulation(x,y,tx,ty,obstacles) where
```
x = Quadcopter starting x-coordinate
y = Quadcopter starting y-coordinate
tx= target x coordinate
ty= target y coordinate
obstacles= number of ibstacles to be randomly generated
```

Move quad around by using the movement(deltax, deltay) method, where

```
deltax = movement in x
deltay = movement in y
```

Read sensor data using the sensor() method with no arguments. It will return "Up", "Down", "Left" or "Right" depending on where it is in relation to an obstacle

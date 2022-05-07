import sys, random, argparse
import math
import turtle
import random
from PIL import Image
from datetime import datetime
from math import gcd 

# constructor
class Spiro:
    # constructor
    def __init__(self, xc, yc, col, R, r, l):
        
        # create the turtle object
        self.t = turtle.Turtle()
        # set the cursor shape
        self.t.shape('turtle')
        # set the step in degrees
        self.step = 5
        # set the drawing complete flag
        self.drawingComplete = False
        
        # set the parameters
        self.setparams(xc, yc, col, R, r, l)

        # initialize the drawing
        self.restart()
    # set the parameters
    def setparams(self, xc, yc, col, R, r, l):
        # set the spirograph parameters
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        # reduce r/R to its smallest form by dividing by GCD
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r//gcdVal
        # get ratio of radii
        self.k = r/float(R)
        # set the color
        self.t.color(*col)
        # store the current angle
        self.a = 0
    
    # restart the drawing
    def restart(self):
        # set the flag
        self.drawingComplete = False
        # show the turtle
        self.t.showturtle()
        # go to the 1st point
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    # draw the whole thing
    def draw(self):
        # draw the rest of the points
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.nRot + 1, self.stop):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        # drawing is now done so hide the turtle cursor
        self.t.hideturtle()

    # update by one step
    def update(self):
        # skip the rest of the steps if done
        if self.drawingComplete: 
            return
        # increment the angle
        self.a += self.step
        # draw a step
        R, k, l = self.R, self.k, self.l
        # set the angle
        a = math.radians(self.a)
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
        self.t.pos(self.xc + x, self.yc + y)
        # if the drawing is complete, set the flag
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            # drawing is now done so hide the turtle cursor
            self.t.hideturtle()

        # clear everything
        def clear(self):
            self.t.clear()
    # a class for animating Spirographs
    class SpiroAnimator:
        # constructor
        def __init__(self, N):
            # set the time value in milliseconds
            self.deltaT = 10
            # get the window dimensions
            self.width = turtle.window.width()
            self.height = turtle.window.height()
            # create the Spiro objects
            self.spiros = []
            for i in range(N):
                # generate random parameters
                rparams = self.genRandamParams()
                # set the spiro parameters
                spiro = Spiro(*rparams)
                self.spiros.append(spiro)
            # call timer
            turtle.ontimer(self.update, self.deltaT)

        # restart spiro drawing
        def restart(self):
            for spiro in self.spiros: 
                # clear
                spiro.clear()
                # generate random parameters
                rparams = self.genRandomParams()
                # set the spiro parameters
                spiro.setparams(*rparams)
                # restart drawing
                spiro.restart()

        # generate random parameters
        def genRandomParams(self):
            width, height = self.width, self.heightR = random.randint(50, min(width, height)//2)
            r = random.randint(10, 9*R//10)
            l = random.uniform(0.1, 0.9)
            xc = random.randint(-width//2, width//2)
            yc = random.randint(-height//2, height//2)
            col = (random.random(), random.random(), random.random())
            return (xc, yc, col, R, r, l)
        
        def update(self):
            # update all spiros
            nComplete = 0
            for spiro in self.spiros:
                # update
                spiro.update()
                # count completed spiros
                if spiro.drawingComplete:
                    nComplete += 1
            # restart if all spiros are complete
            if nComplete == len(slef.spiros):
                self.restart()
            # call the timer
            turtle.ontimer(self.update, self.deltaT)

        # toggle turtle cursor on and off
        def toggleTurtles(self):
            for spiro in self.spiros:
                if spiro.t.isvisible():
                    spiro.t.hideturtle()
                else:
                    spiro.t.showturtle
    
    # save drawings as PNG files
    def saveDrawing():
        # hide the turtle cursor
        turtle.hideturtle()
        # generate unique filenames
        dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
        fileName = 'spiro-' + dateStr
        
from graphics import *
import random
from random import randint

def Randcolor():
    '''generate random color'''
    color=color_rgb( randint( 0, 255 ), randint( 0, 255 ), randint( 0, 255 ))
    return color

class background:
    def __init__(self, win, w, x):
        '''create columns at the bottom'''
        self.x1 = x-30
        self.x2 = x
        self.y1 = randint(-50,20)
        self.y2 = -w
        p1 = Point(self.x1,self.y1)
        p2 = Point(self.x2,self.y2)
        self.rec = Rectangle(p1,p2)

        color = ['powderblue', 'darkcyan', 'darkslategray', 'lightslategray',
                 'lightsteelblue', 'cadetblue']
        color1 = random.choice(color)
        self.rec.setFill(color1)
        self.rec.setOutline(color1)

        self.rec.draw(win)

    def MoveColumn(self,w):
        '''move the column''' 
        p2_move = self.rec.getP2()
        x2_move = p2_move.getX()

        if x2_move <-w:
            self.rec.move(4*w,0)
            self.x1 = self.x1+4*w
            self.x2 = self.x2+4*w
        else:
            dx = -10
            self.rec.move(dx,0)
            self.x1 = self.x1+dx
            self.x2 = self.x2+dx

    def getX1(self):
        return self.x1

    def getX2(self):
        return self.x2

    def getY1(self):
        return self.y1

    def getY2(self):
        return self.y2

from graphics import *
from random import randint

class Pig:
    '''a movable pig'''
    def __init__(self,win):
        self.circ = Circle(Point(0,0),10)
        self.pcent = self.circ.getCenter()
        self.cy = self.pcent.getY()
        self.cx = self.pcent.getX()
        self.circ.setFill('pink')
        self.circ.setOutline('indian red')
        self.text1 = Text(Point(0,6)," ^   ^")
        self.text1.setSize(18)
        self.text = Text(Point(0,-2),"ヾ(；ﾟ(OO)ﾟ)ﾉ")
        self.text2 = Text(Point(-14,-2),"~")
        self.text2.setSize(25)
        self.text.setStyle("bold")
        self.text.setSize(12)
    
        
        self.circ.setWidth(3) 
        self.circ.draw(win)
        self.text1.draw(win)
        self.text.draw(win)
        self.text2.draw(win)
        self.win = win

        

    def movePig(self,dy):   
        self.circ.move(0,dy)
        self.text1.move(0,dy)
        self.text.move(0,dy)
        self.text2.move(0,dy)
        self.cy = self.cy+dy

    def getCX(self):
        return self.cx
            
    def getCY(self):
        return self.cy

    def setCX(self,x):
        self.cx = self.cx+x

    def setCY(self,y):
        self.cy = self.cy+y 

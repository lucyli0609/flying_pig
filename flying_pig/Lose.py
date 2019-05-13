from graphics import *
from random import randint
class Lose:
    def __init__(self,win):
        '''You lose sign'''
        self.rect = Rectangle(Point(-50,-50),Point(50,50))
        self.rect.setFill('rosybrown')
        self.rect.setOutline('white')
        #text
        self.text = Text(Point(0,0),str('YOU LOSE!'))
        self.text.setSize(18)
        self.text.setTextColor('white')
        self.text.setStyle("bold")
        self.rect.draw(win)
        self.text.draw(win)  




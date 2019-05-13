# graphic part for volume control game
#Lucy Li, Yileng Lai, Wanqi Wang

from graphics import *
from random import randint
from Lose import Lose
from background import background
from Pig import Pig
import numpy
import math
import pyaudio

def loudness(chunk):
    '''Calculate and return volume of input samples

    Input chunk should be a numpy array of samples for analysis, as
    returned by sound card.  Sound card should be in 16-bit mono mode.
    Return value is measured in dB, will be from 0dB (maximum
    loudness) down to -80dB (no sound).  Typical very loud sound will
    be -1dB, typical silence is -36dB.

    '''
    data = numpy.array(chunk, dtype=float) / 32768.0
    ms = math.sqrt(numpy.sum(data ** 2.0) / len(data))
    if ms < 10e-8: ms = 10e-8
    return 10.0 * math.log(ms, 10.0)

def isInside(pig,Lcolumn):
    '''a function to determine whether the pig catch the column'''
    cx = pig.getCX()
    cy = pig.getCY()

    LX1 = []
    LY1 = []
    LX2 = []
    LY2 = []
    for col in Lcolumn:
        x1 = col.getX1()
        x2 = col.getX2()
        y1 = col.getY1()
        y2 = col.getY2()
        LX1.append(x1)
        LX2.append(x2)
        LY1.append(y1)
        LY2.append(y2)
    
    for i in range(len(LX1)):
        if (((cx)<LX2[i])&((cx)>LX1[i])&((cy)>LY2[i])&((cy)<LY1[i])):
            return False
                                    
def main( ):
    #set up pyaudio
    pyaud = pyaudio.PyAudio()
    #open input stream
    stream = pyaud.open(
        format = pyaudio.paInt16,
        channels = 1,
        rate = 48000,
        input_device_index = None,
        input = True)
    
    #set up graphic window
    win = GraphWin( 'Flying Pig', 900, 900, autoflush=False )
    win.setBackground( 'gainsboro' )
    w=100
    win.setCoords( -w, -w, w, w )

    #create background columns
    x = [100,180,250,330,410,500]
    Lcolumn = []
    for i in range(5):        
        bg = background(win,w,x[i])
        Lcolumn.append(bg)
        
    #create pig
    pig = Pig(win)
    
    # get pig and column moving
    count = 0
    text = Text(Point(-75,80), '')
    while True:
        p = win.checkMouse()
        key = win.checkKey( )
        cy = pig.getCY()
        # Read raw microphone data
        try:
            rawsamps = stream.read(50000, exception_on_overflow = False)
        except OSError as e:
            return print("wait a moment please")
        # Convert raw data to NumPy array
        else:
           samps = numpy.fromstring(rawsamps, dtype=numpy.int16)

        if (cy >-95) & (cy < 130):
            pig.movePig(-1)
            #set score
            count = count + 1
            text.undraw()
            score = Text(Point(-88,80), 'Score: ')
            score.setSize(18)
            score.draw(win)
            text = Text(Point(-72,80), count)
            text.setSize(18)
            text.draw(win)
            #set different loundness level
            if (loudness(samps) > (-8)):
                pig.movePig(5)
            elif (loudness(samps) > (-5)):
                pig.movePig(8)
            elif (loudness(samps) > (-2)):
                pig.movePig(10)
            # if pig crashes on the column, game over
            if isInside(pig,Lcolumn)==False:
                lose = Lose(win)
                break
        else: # if pig out of window range, game over
            lose = Lose(win)
            break
        
        if p == None:
            for i in range(5):
                Lcolumn[i].MoveColumn(w)
        elif p: 
             break
    
    #close window
    win.getMouse()
    win.close()

main()

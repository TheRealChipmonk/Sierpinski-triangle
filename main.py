import numpy as np
import scipy.misc as smp
import random
from random import randrange
from PIL import Image, ImageDraw

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

def getmiddle(A,B):
    return (A+B)/2

iterations = 500000

im = Image.new('RGB', (500, 500), (255,255,255))
draw = ImageDraw.Draw(im)

triSize = 100

A = Point(250, 0)
B = Point(0, 500)
C = Point(500, 500)


#Draw first points
draw.point((A.x,A.y), fill=(0,0,0))
draw.point((B.x,B.y), fill=(0,0,0))
draw.point((C.x,C.y), fill=(0,0,0))

#pick first random point
ranPoint = Point(randrange(50, 250), (randrange(10, 150)))
sav = randrange(4)

for temp in range(iterations):
    ran = randrange(3)
    if ran == 0:
        newX = getmiddle(A.x, ranPoint.x)
        newY = getmiddle(A.y, ranPoint.y)
        draw.point((newX, newY), fill=(0, 0, 0))
        ranPoint = Point(newX, newY)

    if ran == 1:
        newX = getmiddle(B.x, ranPoint.x)
        newY = getmiddle(B.y, ranPoint.y)
        draw.point((newX, newY), fill=(0, 0, 0))
        ranPoint = Point(newX, newY)

    if ran == 2:
        newX = getmiddle(C.x, ranPoint.x)
        newY = getmiddle(C.y, ranPoint.y)
        draw.point((newX, newY), fill=(0, 0, 0))
        ranPoint = Point(newX, newY)





im.show()
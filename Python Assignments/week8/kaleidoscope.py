from tkinter import *
import random

def makeRandomDiamonds(nbrDiamonds, width, height, minSize, maxSize):
    shapeList = []
    for _ in range(nbrDiamonds):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(minSize, maxSize)
        colour = random.choice(['red', 'green', 'blue', 'cyan', 'yellow','magenta'])
        diamond = {'x':x, 'y':y, 'size':size, 'colour':colour}
        shapeList.append(diamond)
    return shapeList

def showDiamond(canvas,diamond):
  xcen = diamond['x']
  ycen = diamond['y']
  w = diamond['size']/2
  canvas.create_polygon(xcen,ycen-w,
                               xcen + w, ycen,
                               xcen,ycen + w,
                               xcen-w,ycen,fill = diamond['colour'])


def reflectV(diamond,xval):
  reflected = {}
  reflected['x'] = 2*xval-diamond['x']
  reflected['y'] = diamond['y']
  reflected['size'] = diamond['size']
  reflected['colour'] = diamond['colour']
  
  return reflected


def reflectH(diamond,yval):
  reflected = {}
  reflected['x'] = diamond['x']
  reflected['y'] = 2*yval-diamond['y']
  reflected['size'] = diamond['size']
  reflected['colour'] = diamond['colour']
  
  return reflected


def reflectD(diamond):
  reflected = {}
  reflected['x'] = diamond['y']
  reflected['y'] = diamond['x']
  reflected['size'] = diamond['size']
  reflected['colour'] = diamond['colour']
  return reflected

#main program
width = 300
height = 300
root = Tk()
canvas = Canvas(root, width=width,height=height)
canvas.pack()
    
for d in makeRandomDiamonds(70, width, height, width/20, width/15):
    showDiamond(canvas,d)
    shapes1 = [d,reflectH(d,height/2)]
    shapes2 = []
    for s in shapes1:
        shapes2.append(s)
        shapes2.append(reflectV(s,width/2))
    shapes3 = []
    for s in shapes2:
        shapes3.append(s)
        shapes3.append(reflectD(s))
    for s in shapes3:
        showDiamond(canvas,s)
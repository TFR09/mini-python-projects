from tkinter import *

def showDiamond(canvas,diamond):
    xcen = diamond['x']
    ycen = diamond['y']
    w = diamond['size']/2
    canvas.create_polygon(xcen,ycen-w,
                                xcen + w, ycen,
                                xcen,ycen + w,
                                xcen-w,ycen,fill = diamond['colour'])


def main():
    width = 200
    height = 200
    
    root = Tk()
    canvas = Canvas(root, width=width,height=height)
    canvas.pack()
    diamond = {'x':width/2, 'y':height/2, 'size':width/4, 'colour':'red'}
    showDiamond(canvas,diamond)


if __name__ == "__main__":
    main()
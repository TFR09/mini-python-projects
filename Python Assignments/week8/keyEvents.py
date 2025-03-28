from tkinter import Tk,Canvas

def SclickHandler(event):
    # coords of centre of square
    xcen = event.x 
    ycen = event.y
    hw = 30 #half the width
    canvas.create_rectangle(xcen - hw,ycen - hw,
                            xcen + hw,ycen + hw,
                            fill = 'magenta')
    

def CclickHandler(event):
    # coords of centre of square
    xcen = event.x 
    ycen = event.y
    hw = 30 #half the width
    canvas.create_oval(xcen - hw,ycen - hw,
                            xcen + hw,ycen + hw,
                            fill = 'magenta')


def DclickHandler(event):
    # coords of centre of square
    xcen = event.x 
    ycen = event.y
    nearId = canvas.find_closest(xcen,ycen)
    canvas.itemconfigure(nearId,fill='black')


def main():
    global canvas
    
    root = Tk()
    canvas = Canvas(root,width=300,height = 300)
    canvas.pack()
    canvas.bind('<Shift-Button-1>',SclickHandler)
    canvas.bind('<Control-Button-1>',CclickHandler)
    canvas.bind('<Double-Button-1>',DclickHandler)
    root.mainloop()
  
if __name__ == "__main__":
    main()
from tkinter import *

x1 = -1
y1 = -1

def clickHandler(event):
  global x1,y1
  if x1 < 0:
    pass
  else:
    canvas.create_line(x1,y1,event.x,event.y,width=2,fill = 'white')
    x1 = event.x
    y1 = event.y

root = Tk()
root.title("Sketch Pad")
canvas = Canvas(root,width=300,height=300, bg='black')
canvas.pack()
canvas.bind('<Button-1>',clickHandler)
  
root.mainloop()
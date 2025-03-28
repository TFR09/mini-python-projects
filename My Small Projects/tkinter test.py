from tkinter import *

def clear():
  canvas.delete('all')

def clickHandler(event):
  global shape
  xcen = event.x
  ycen = event.y
  hw = 30
  if shape.get() == 'Square':
    canvas.create_rectangle(xcen - hw,ycen - hw,xcen + hw,ycen + hw,fill='magenta')
  elif shape.get() == 'Diamond':
    canvas.create_polygon(xcen,ycen - hw,xcen + hw,ycen,xcen,ycen + hw,xcen - hw,ycen,fill='magenta')
  elif shape.get == 'Text':
    canvas.create_text(text = theText)

if __name__ == "__main__":
  root = Tk()
  entry = Entry(root)
  entry.grid(row = 0,columnspan = 2, sticky = 'EW')
  theText = entry.get()
  button = Button(root, text='Clear', command=clear)

  button.grid(row=3, columnspan=2, sticky='EW')
  shape = StringVar()
  shape.set('Square')
  rsquare = Radiobutton(root, text='Square', variable=shape, value='Square')
  rsquare.grid(row=1, column=0)
  rdiamond = Radiobutton(root,text='Diamond',variable=shape,value='Diamond')
  rdiamond.grid(row=1, column=1)
  rtext = Radiobutton(root,text = 'Text',variable=shape,value = 'Text')
  rtext.grid(row=1, column=2)
  canvas = Canvas(root, width=500, height=500)
  canvas.bind('<Button-1>', clickHandler)
  canvas.grid(row=3, columnspan=3, sticky='NSEW')

  root.mainloop()

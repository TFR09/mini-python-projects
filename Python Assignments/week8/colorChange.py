from tkinter import *

def change():
    if colour == 'red':
        colour = 'green'
    else:
        colour = 'red'
    canvas.itemconfigure(circle,fill=colour)

def main():
    global colour, canvas

    root = Tk()
    root.title('Change Colour')
    canvas = Canvas(root, width=300,height=300)
    canvas.grid(row=1,column=0,columnspan=3)
    button = Button(root, text = 'Change', command = change,padx = 50)
    button.grid(row=0,column=0,columnspan=3)
    colour = 'red'
    circle = canvas.create_oval(25,275,275,25,fill=colour, outline = 'black')


if __name__ == "__main__":
    main()
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.resizable(0,0)
root.configure(background="black")
root.title("Virtual Assistant GUI Test")

canvas = tk.Canvas(root, width=800,height=600,bg="black",highlightbackground="black")
canvas.grid(columnspan=3)

image = Image.open('VA.gif')
img = ImageTk.PhotoImage(image)
logo_label = tk.Label(root, image=img,highlightthickness=0).grid(column=1,row=0)

pht = tk.Label(root, text="Sample text for a VA GUI app using Tkinter",font=('Courier',20),bg="black",fg="white")
pht.grid(columnspan=3,row=1, column=0)

def click():
    sample=tk.Label(root)
    sample.configure(text="Clicking on the button does nothing for now!",font=('Courier',20),bg="black",fg="white")
    sample.grid(columnspan=3, column=0, row=3)

button = tk.Button(root,text="Listen",font=('Courier',20),command=click).grid(columnspan=3,column=0,row=2)
canvas = tk.Canvas(root, width=800,height=200,bg="black",highlightthickness=0).grid(columnspan=3)


root.mainloop()
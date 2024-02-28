from tkinter import *

window = Tk()

def btn_clicked():
    print("Button Clicked")


Btn = Button(window, text="Click Me!", command=btn_clicked)

Btn.pack()

window.mainloop()




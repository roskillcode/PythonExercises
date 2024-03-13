from tkinter import *

window = Tk()

window.geometry("200x200")

def red_clicked():
    window.configure(bg='red')
    
def blue_clicked():
    window.configure(bg='blue')

redbtn = Button(window, text="Red", command=red_clicked)
bluebtn = Button(window, text="Blue", command=blue_clicked)

redbtn.pack()
bluebtn.pack()

window.mainloop()



from tkinter import *
window = Tk()
window.title("Animal de companie")

bortin = Button(text="bortin")
n =[bortin]
for c in n:
    c.grid(column=1, row=0)

window.mainloop()
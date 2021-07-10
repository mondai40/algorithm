from tkinter import *

root = Tk()
root.title("Hello world")
root.geometry("500x500")

label = Label(root, text="Name")
entry = Entry(root)
label.grid(row=0, column=0)
entry.grid(row=0, column=1)

root.mainloop()
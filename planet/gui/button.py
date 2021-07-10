from tkinter import *

root = Tk()
root.title("First button")
root.geometry("500x500")

button1 = Button(root, text="Submit1", fg="blue", bg="yellow")
button2= Button(root, text="Submit2", fg="blue", bg="yellow")
button3 = Button(root, text="Submit3", fg="blue", bg="yellow")
button4 = Button(root, text="Submit4", fg="blue", bg="yellow")

button1.grid(row=0, column=0)
button2.grid(row=0, column=2)
button3.grid(row=1, column=5)
button4.grid(row=4, column=3)


root.mainloop()



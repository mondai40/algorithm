from tkinter import *

root = Tk()
root.title("First label")
root.geometry("200x200")

# labelの作成, *** 編集不可 ***
# 一番シンプルなやつ
# course = Label(root, text="This is first label.")
# 色付き
course = Label(root, text="Text with foreground and background color", bg="red", fg="yellow")

# labelの設置。これがないとGui上に表示されない
course.pack()

root.mainloop()

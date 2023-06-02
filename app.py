from tkinter import *

root = Tk()
root.title("Hello")
root.geometry("1600x1600")

class marks:
    def class_1(self):
        label_1["text"] = "83%"
    def class_2(self):
        label_2["text"] = "93%"
    def class_3(self):
        label_3["text"] = "99.99%"

Students_Marks = marks()

button_1 = Button(root, text="Class 1", command=Students_Marks.class_1)
button_1.pack()

label_1 = Label(root)
label_1.pack()

button_2 = Button(root, text="Class 2", command=Students_Marks.class_2)
button_2.pack()

label_2 = Label(root)
label_2.pack()

button_3 = Button(root, text="Class 3", command=Students_Marks.class_3)
button_3.pack()

label_3 = Label(root)
label_3.pack()

root.mainloop()
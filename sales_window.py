from tkinter import *
import tkinter.messagebox as mb
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase1"

)
mycur = mydb.cursor()
print("connected to db")


class manager_window:
    def __init__(self):
        self.root = Tk()
        self.root.title("welcome")
        self.root.geometry("500x300")

    def run(self):
        self.root.mainloop()


class employee():
    def __init__(self):
        self.emp_window = Tk()
        self.emp_window.geometry("990x600")
        self.emp_window.title("product details")
        self.label1 = Label(self.emp_window, text="Bill No :", font="times 15 bold")
        self.label1.place(x=10, y=20)
        self.ent1 = Entry(self.emp_window)
        self.ent1.place(x=90, y=20)
        self.btn_search = Button(self.emp_window, text="Search", font="times 15 bold")
        self.btn_search.place(x=260, y=20)

        self.label2 = Label(self.emp_window, text="Customer Name :", font="times 14 bold")
        self.label2.place(x=380, y=20)
        self.ent_name = Entry(self.emp_window)
        self.ent_name.place(x=540, y=20)
        self.label3 = Label(self.emp_window, text="Phone No :", font="times 14 bold")
        self.label3.place(x=730, y=20)
        self.ent_phn = Entry(self.emp_window)
        self.ent_phn.place(x=840, y=20)
        self.label5 = Label(self.emp_window, text="category", font="times 14")
        self.label5.place(x=20, y=90)
        self.ent_1 = Entry(self.emp_window)
        self.ent_1.place(x=100, y=90)
        self.label6 = Label(self.emp_window, text="category", font="times 14")
        self.label6.place(x=20, y=140)
        self.ent_1 = Entry(self.emp_window)
        self.ent_1.place(x=100, y=140)
        self.label7 = Label(self.emp_window, text="category", font="times 14")
        self.label7.place(x=20, y=190)
        self.ent_1 = Entry(self.emp_window)
        self.ent_1.place(x=100, y=190)
        self.label8 = Label(self.emp_window, text="category", font="times 14")
        self.label8.place(x=20, y=240)
        self.ent_1 = Entry(self.emp_window)
        self.ent_1.place(x=100, y=240)

    def run(self):
        self.emp_window.mainloop()


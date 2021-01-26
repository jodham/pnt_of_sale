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
        self.label5 = Label(self.emp_window, text="Category", font="times 14")
        self.label5.place(x=20, y=90)
        self.ent_categ = Entry(self.emp_window)
        self.ent_categ.place(x=130, y=90)
        self.label6 = Label(self.emp_window, text="Sub-Category", font="times 14")
        self.label6.place(x=20, y=140)
        self.ent_sub_categ = Entry(self.emp_window)
        self.ent_sub_categ.place(x=130, y=140)
        self.label7 = Label(self.emp_window, text="Product", font="times 14")
        self.label7.place(x=20, y=190)
        self.ent_produc = Entry(self.emp_window)
        self.ent_produc.place(x=130, y=190)
        self.label8 = Label(self.emp_window, text="Quantity", font="times 14")
        self.label8.place(x=20, y=240)
        self.ent_quant = Entry(self.emp_window)
        self.ent_quant.place(x=130, y=240)
        self.Btn_add = Button(self.emp_window, text="Add to cart", font="times 9 bold")
        self.Btn_add.place(x=25, y=280)
        self.btn_clear = Button(self.emp_window, text="Clear", font="times 9 bold")
        self.btn_clear.place(x=130, y=280)

    # -----------------------------------------calculator------------------
        self.display_ent = Entry(self.emp_window)
        self.display_ent.place(x=340, y=90)
        self.btn7 = Button(self.emp_window, text="7", font='times 9 bold')
        self.btn7.place(x=340, y=120)
        self.btn8 = Button(self.emp_window, text="8", font='times 9 bold')
        self.btn8.place(x=380, y=120)
        self.btn9 = Button(self.emp_window, text="9", font='times 9 bold')
        self.btn9.place(x=420, y=120)
        self.btn_add = Button(self.emp_window, text="+", font='times 9 bold')
        self.btn_add.place(x=460, y=120)
        self.btn6 = Button(self.emp_window, text="6", font='times 9 bold')
        self.btn6.place(x=340, y=160)
        self.btn5 = Button(self.emp_window, text="5", font='times 9 bold')
        self.btn5.place(x=380, y=160)
        self.btn4 = Button(self.emp_window, text="4", font='times 9 bold')
        self.btn4.place(x=420, y=160)
        self.btn_multiply = Button(self.emp_window, text="*", font='times 9 bold')
        self.btn_multiply.place(x=460, y=160)
        self.btn3 = Button(self.emp_window, text="3", font='times 9 bold')
        self.btn3.place(x=340, y=200)
        self.btn2 = Button(self.emp_window, text="2", font='times 9 bold')
        self.btn2.place(x=380, y=200)
        self.btn1 = Button(self.emp_window, text="1", font='times 9 bold')
        self.btn1.place(x=420, y=200)
        self.btn_division = Button(self.emp_window, text="/", font='times 9 bold')
        self.btn_division.place(x=460, y=200)
        self.btn0 = Button(self.emp_window, text="0", font='times 9 bold')
        self.btn0.place(x=340, y=240)
        self.btn_dot = Button(self.emp_window, text=".", font='times 9 bold')
        self.btn_dot.place(x=380, y=240)
        self.btn_equal = Button(self.emp_window, text="=", font='times 9 bold')
        self.btn_equal.place(x=420, y=240)
        self.btn_sub = Button(self.emp_window, text="-", font='times 9 bold')
        self.btn_sub.place(x=460, y=240)
    # ------------------------------------------calculator-------------------

    def run(self):
        self.emp_window.mainloop()

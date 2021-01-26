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
        self.canva = Canvas(self.emp_window, bg="blue", height=200, width=200)
        self.canva.place(x=320, y=90)

    # -----------------------------------------calculator------------------
        #display_ent = Entry(self.canva)
        #display_ent.pack()
    # ------------------------------------------calculator-------------------

    def run(self):
        self.emp_window.mainloop()

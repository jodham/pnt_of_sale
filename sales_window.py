from tkinter import *
import tkinter.messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase1"
)
mycur = mydb.cursor()


class manager_window:
    def __init__(self):
        self.root = Tk()
        self.root.title("welcome")
        self.root.geometry("990x500")
        self.label1 = Label(self.root, text="RETAIL MANAGEMENT SYSTEM", font="times 20 bold")
        self.label1.place(x=400, y=5)
        self.title_frame = Frame(self.root, bd=10, relief=GROOVE)
        self.title_frame.place(x=200, y=40, width=600, height=50)
        self.title_frame.config(bg="blue")
        self.add_user_btn = Button(self.title_frame, text="Add User", font="Aerial 10 bold", command=self.add_user)
        self.add_user_btn.place(x=2, y=1)
        self.add_prod_btn = Button(self.title_frame, text="Add Product", font="Aerial 10 bold", command=self.new_product)
        self.add_prod_btn.place(x=120, y=1)
        self.chek_price_btn = Button(self.title_frame, text="Price Check", font="Aerial 10 bold",
                                     command=self.price_check)
        self.chek_price_btn.place(x=270, y=1)
        self.chek_stock_btn = Button(self.title_frame, text="Stock Check", font="Aerial 10 bold", command=self.stock)
        self.chek_stock_btn.place(x=410, y=1)
        self.side_frame = Frame(self.root, bd=10, relief=GROOVE)
        self.side_frame.place(x=200, y=100, width=110, height=400)
        self.side_frame.config(bg="white")
        self.display_frame = Frame(self.root, bd=10, relief=GROOVE)
        self.display_frame.place(x=320, y=100, width=600, height=400)
        self.display_frame.config(bg="white")
        self.product_display_btn = Button(self.side_frame, text="Products", font="Aerial 8 bold")
        self.product_display_btn.place(x=1, y=1, height=60, width=90)
        self.employees_btn = Button(self.side_frame, text="Employees", font="Aerial 8 bold")
        self.employees_btn.place(x=1, y=60, height=60)
        self.users_btn = Button(self.side_frame, text="Users", font="Aerial 8 bold")
        self.users_btn.place(x=1, y=120, height=60, width=90)
        self.supplier_btn = Button(self.side_frame, text="Supplier", font="Aerial 8 bold")
        self.supplier_btn.place(x=1, y=180, height=60, width=90)
        self.password_btn = Button(self.side_frame, text="Change", font="Aerial 8 bold")
        self.password_btn.place(x=1, y=240, height=60, width=90)
        self.about_btn = Button(self.side_frame, text="About", font="Aerial 8 bold")
        self.about_btn.place(x=1, y=300, height=60, width=90)

    def add_user(self):
        self.add_user_frame = Frame(self.root, bd=10, relief=GROOVE)
        self.add_user_frame.place(x=400, y=100, width=400, height=400)
        self.add_user_frame.config(bg="blue")
        self.lbl1 = Label(self.add_user_frame, text="Add User", font="Aerial 25 bold")
        self.lbl1.place(x=100, y=20)
        self.lbl1.config(bg="blue", fg="white")
        self.exit_btn = Button(self.add_user_frame, text="X", font="times 20 bold", command=self.add_user_frame.destroy)
        self.exit_btn.place(x=330, y=5)
        self.label_name = Label(self.add_user_frame, text="Username :", font="Aerial 14 bold")
        self.label_name.place(x=30, y=100)
        self.label_name.config(bg="blue", fg="white")
        self.user_ent = Entry(self.add_user_frame)
        self.user_ent.place(x=170, y=100)
        self.label_id = Label(self.add_user_frame, text="ID             :", font="Aerial 14 bold")
        self.label_id.place(x=30, y=150)
        self.label_id.config(bg="blue", fg="white")
        self.id_ent = Entry(self.add_user_frame)
        self.id_ent.place(x=170, y=150)
        self.label_psw = Label(self.add_user_frame, text="Password  :", font="Aerial 14 bold")
        self.label_psw.place(x=30, y=200)
        self.label_psw.config(bg="blue", fg="white")
        self.psw_ent = Entry(self.add_user_frame, show="*")
        self.psw_ent.place(x=170, y=200)
        self.label_categ = Label(self.add_user_frame, text="Category  :", font="Aerial 14 bold")
        self.label_categ.place(x=30, y=250)
        self.label_categ.config(bg="blue", fg="white")
        self.categ_ent = Entry(self.add_user_frame)
        self.categ_ent.place(x=170, y=250)
        self.add_btn = Button(self.add_user_frame, text="Add", font="Aerial 14 bold", command=self.new_user)
        self.add_btn.place(x=60, y=320)
        self.clear_btn = Button(self.add_user_frame, text="Clear", font="Aerial 14 bold", command=self.clear)
        self.clear_btn.place(x=150, y=320)

    def clear(self):
        self.user_ent.delete(0, END)
        self.id_ent.delete(0, END)
        self.psw_ent.delete(0, END)
        self.categ_ent.delete(0, END)

    def new_user(self):
        cusId = self.id_ent.get()
        username = self.user_ent.get()
        password = self.psw_ent.get()
        category = self.categ_ent.get()
        if cusId or username or password or category != "":
            sql = "INSERT INTO tbl_user(id, username, password, category) VALUES (%s,%s,%s,%s)"
            val = (cusId, username, password, category)
            mycur.execute(sql, val)

            mydb.commit()
            tkinter.messagebox.showinfo("success!!", category + " " + "added")
            self.user_ent.delete(0, END)
            self.id_ent.delete(0, END)
            self.psw_ent.delete(0, END)
            self.categ_ent.delete(0, END)
        else:
            tkinter.messagebox.showerror("null value", "fill all fields")

    def run(self):
        self.root.mainloop()

    def new_product(self):
        self.add_product_frame = Frame(self.root, bd=10, relief=GROOVE)
        self.add_product_frame.place(x=320, y=100, width=600, height=400)
        self.add_product_frame.config(bg="blue")
        self.exit_btn = Button(self.add_product_frame, text="X", font="times 20 bold",
                               command=self.add_product_frame.destroy)
        self.exit_btn.place(x=530, y=5)
        self.label = Label(self.add_product_frame, text="Add product", font="Aerial 20 bold")
        self.label.place(x=200, y=5)
        self.label.config(bg="blue")
        self.label2 = Label(self.add_product_frame, text="Product Code", font="Aerial 12 bold")
        self.label2.place(x=30, y=60)
        self.label2.config(bg='blue')
        self.label3 = Label(self.add_product_frame, text="Product Name", font="Aerial 12 bold")
        self.label3.place(x=30, y=100)
        self.label3.config(bg='blue')
        self.label4 = Label(self.add_product_frame, text="Category", font="Aerial 12 bold")
        self.label4.place(x=30, y=140)
        self.label4.config(bg='blue')
        self.label5 = Label(self.add_product_frame, text="Quantity", font="Aerial 12 bold")
        self.label5.place(x=30, y=180)
        self.label5.config(bg='blue')
        self.label6 = Label(self.add_product_frame, text="Price/Unit", font="Aerial 12 bold")
        self.label6.place(x=30, y=220)
        self.label6.config(bg='blue')
        self.product_code = Entry(self.add_product_frame)
        self.product_code.place(x=170, y=60)
        self.search_btn = Button(self.add_product_frame, text="Search", font="Aerial 12 bold")
        self.search_btn.place(x=390, y=60)
        self.product_Name = Entry(self.add_product_frame)
        self.product_Name.place(x=170, y=100)
        self.categ_ent = Entry(self.add_product_frame)
        self.categ_ent.place(x=170, y=140)
        self.quantity_ent = Entry(self.add_product_frame)
        self.quantity_ent.place(x=170, y=180)
        self.price_ent = Entry(self.add_product_frame)
        self.price_ent.place(x=170, y=220)
        self.add_button = Button(self.add_product_frame, text="Add", font="Aerial 12 bold", command=self.add_product)
        self.add_button.place(x=140, y=300)
        self.clear_button = Button(self.add_product_frame, text="Clear", font="Aerial 12 bold", command=self.reset)
        self.clear_button.place(x=280, y=300)

    def reset(self):
        self.product_code.delete(0, END)
        self.product_Name.delete(0, END)
        self.categ_ent.delete(0, END)
        self.quantity_ent.delete(0, END)
        self.price_ent.delete(0, END)

    def add_product(self):
        procode = self.product_code.get()
        proName = self.product_Name.get()
        category1 = self.categ_ent.get()
        quantity_ent = self.quantity_ent.get()
        price = self.price_ent.get()

        if procode or category1 or quantity_ent or price or proName != "":
            query = "INSERT INTO tbl_product(productCode, productName, category, quantity, unitPrice) VALUES (%s,%s,%s,%s,%s)"
            mydata = (procode, proName, category1, quantity_ent, price)
            try:
             mycur.execute(query, mydata)
            except mysql.connector.Error as e:
                try:
                    tkinter.messagebox.showerror("duplicate","product"+" "+procode +" "+"Exists")
                   # print("MYsql Error [%d]: %s" %(e.args[0], e.args[1]))
                    return None
                except IndexError:
                    print("MySQL Error: %s" %str(e))
                    return None
            except TypeError as e:
                print(e)
                return None
            except ValueError as e:
                print(e)
                return None

            else:
                mydb.commit()
                tkinter.messagebox.showinfo("success!!", "product added")

        else:
            tkinter.messagebox.showerror("null value", "fill all values")

    def price_check(self):
        self.add_price_frame = Frame(self.root, bd=10, relief=GROOVE)
        self.add_price_frame.place(x=320, y=100, width=600, height=400)
        self.add_price_frame.config(bg="blue")
        self.exit_btn = Button(self.add_price_frame, text="X", font="times 20 bold",
                               command=self.add_price_frame.destroy)
        self.exit_btn.place(x=530, y=5)

    def stock(self):
        self.stock_frame = Frame(self.root, bd=10, relief=GROOVE)
        self.stock_frame.place(x=320, y=100, width=600, height=400)
        self.stock_frame.config(bg="blue")
        self.exit_btn = Button(self.stock_frame, text="X", font="times 20 bold", command=self.stock_frame.destroy)
        self.exit_btn.place(x=530, y=5)


class employee():
    def __init__(self):
        self.emp_window = Tk()
        self.emp_window.geometry("990x600")
        self.emp_window.title("product details")
        self.label1 = Label(self.emp_window, text="Product Name :", font="times 15 bold")
        self.label1.place(x=10, y=20)
        self.ent1 = Entry(self.emp_window)
        self.ent1.place(x=160, y=20)
        self.btn_search = Button(self.emp_window, text="Search", font="times 15 bold")
        self.btn_search.place(x=330, y=20, width=59)
        self.btn_search.config(bg='yellow')

        self.label2 = Label(self.emp_window, text="Customer Name :", font="times 14 bold")
        self.label2.place(x=410, y=20)
        self.ent_name = Entry(self.emp_window)
        self.ent_name.place(x=570, y=20)
        self.label3 = Label(self.emp_window, text="Phone No :", font="times 14 bold")
        self.label3.place(x=730, y=20)
        self.ent_phn = Entry(self.emp_window)
        self.ent_phn.place(x=820, y=20)
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
        self.Btn_add = Button(self.emp_window, text="Add to cart", font="Aerial 15 bold")
        self.Btn_add.place(x=25, y=300)
        self.btn_clear = Button(self.emp_window, text="Clear", font="Aerial 15 bold")
        self.btn_clear.place(x=250, y=300)
        self.frm1 = Frame(self.emp_window, bd=10, relief=GROOVE)
        self.frm1.place(x=25, y=400, width=420, height=90)
        self.btn_total = Button(self.frm1, text="Total", font="Aerial 15 bold")
        self.btn_total.place(x=2, y=13)
        self.btn_total = Button(self.frm1, text="Bill", font="Aerial 15 bold")
        self.btn_total.place(x=150, y=13)
        self.btn_total = Button(self.frm1, text="Exit", font="Aerial 15 bold")
        self.btn_total.place(x=270, y=13)

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
        # =================================================bill area====================
        self.frame = Frame(self.emp_window, bd=10, relief=GROOVE)
        self.frame.place(x=560, y=60, width=350, height=380)
        self.bill_title = Label(self.frame, text="BILL Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=Y)
        scrol_y = Scrollbar(self.frame, orient=VERTICAL)
        self.txtarea = Text(self.frame, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=X)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =================================================bill area====================
    def run(self):
        self.emp_window.mainloop()

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

        if procode or proName or category1 or quantity_ent or price !="":

            query = "INSERT INTO tbl_product(productCode, productName, category, quantity, unitPrice) VALUES (%s,%s,%s,%s,%s)"
            mydata = (procode, proName, category1, quantity_ent, price)
            try:
                mycur.execute(query, mydata)
            except mysql.connector.Error:
                tkinter.messagebox.showerror("duplicate", "product" + " " + procode + " " + "Exists")
                return None
            except IndexError as e:
                print("MySQL Error: %s" % str(e))
                return None
            except TypeError as e:
                print(e)
                return None
            except ValueError:
                tkinter.messagebox.showerror("error", "float value or int expected")
                return None

            else:
                mydb.commit()
                tkinter.messagebox.showinfo("success!!", "product added")
        elif self.quantity_ent or self.price_ent != float:
            raise ValueError
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
        self.label1 = Label(self.emp_window, text="Product Code :", font="times 15 bold")
        self.label1.place(x=10, y=20)
        self.search_code = Entry(self.emp_window)
        self.search_code.place(x=160, y=20)
        self.btn_search = Button(self.emp_window, text="Search", font="times 15 bold", command=self.search_pro)
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
        self.label5 = Label(self.emp_window, text="Product Name", font="times 14")
        self.label5.place(x=20, y=90)
        self.proName_ent = Entry(self.emp_window)
        self.proName_ent.place(x=130, y=90)
        self.label6 = Label(self.emp_window, text="Category", font="times 14")
        self.label6.place(x=20, y=140)
        self.ent_categ = Entry(self.emp_window)
        self.ent_categ.place(x=130, y=140)
        self.label7 = Label(self.emp_window, text="Price/unit", font="times 14")
        self.label7.place(x=20, y=190)
        self.ent_price = Entry(self.emp_window)
        self.ent_price.place(x=130, y=190)
        self.label8 = Label(self.emp_window, text="Quantity", font="times 14")
        self.label8.place(x=20, y=240)
        self.quantitylabel = Label(self.emp_window, text="available", font="Aerial 10 bold")
        self.quantitylabel.place(x=350, y=240)
        self.quantAvailabel = Entry(self.emp_window)
        self.quantAvailabel.place(x=300, y=240, width=45)
        self.ent_quant = Entry(self.emp_window)
        self.ent_quant.place(x=130, y=240)
        self.Btn_add_cart = Button(self.emp_window, text="Add to cart", font="Aerial 15 bold", command=self.add_cart)
        self.Btn_add_cart.place(x=25, y=300)
        self.btn_clear = Button(self.emp_window, text="Clear", font="Aerial 15 bold", command=self.reset)
        self.btn_clear.place(x=250, y=300)
        self.frm1 = Frame(self.emp_window, bd=10, relief=GROOVE)
        self.frm1.place(x=450, y=500, width=420, height=90)
        self.btn_total = Button(self.frm1, text="Total", font="Aerial 15 bold", command=self.totalguds)
        self.btn_total.place(x=2, y=13)
        self.btn_total = Button(self.frm1, text="Bill", font="Aerial 15 bold")
        self.btn_total.place(x=150, y=13)
        self.btn_total = Button(self.frm1, text="Done", font="Aerial 15 bold")
        self.btn_total.place(x=270, y=13)
        # =================================================bill area====================
        self.frame = Frame(self.emp_window, bd=10, relief=GROOVE)
        self.frame.place(x=450, y=60, width=350, height=380)
        self.bill_title = Label(self.frame, text="BILL Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=Y)
        scrol_y = Scrollbar(self.frame, orient=VERTICAL)
        self.txtarea = Text(self.frame, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=X)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        self.txtarea.config(bg="white")
        self.txtframe = Frame(self.txtarea, height=115)
        self.txtframe.pack(fill="x", pady=1)
        self.txtframe.config(bg="white")
        self.shoplabel = Label(self.txtframe, text="Hawaii shoppers !!!", font="Aerial 10 bold")
        self.shoplabel.place(x=60, y=10)
        self.shoplabel.config(bg="white")
        self.shoplabel = Label(self.txtframe, text="shop with us", font="Aerial 10 bold")
        self.shoplabel.place(x=60, y=40)
        self.shoplabel.config(bg="white")
        self.shoplabel = Label(self.txtframe, text="===========================",
                               font="Aerial 10 bold")
        self.shoplabel.place(x=2, y=70)
        self.shoplabel.config(bg="white")
        self.tagLabel = Label(self.txtarea, text="Name.            price/unit.          qnty.          total.")
        self.tagLabel.place(x=2, y=90)
        self.tagLabel.config(bg="white")
        # =================================================bill area====================
        self.paylabel = Label(self.emp_window, text="Amount paid", font="Aerial 12 bold")
        self.paylabel.place(x=800, y=160)
        self.pay_ent = Entry(self.emp_window)
        self.pay_ent.place(x=800, y=200)
        self.totalpaylabel = Label(self.emp_window, text="Cost of Goods", font="Aerial 12 bold")
        self.totalpaylabel.place(x=800, y=60)
        self.totalguds = Entry(self.emp_window)
        self.totalguds.place(x=800, y=100)
        self.balancelabel = Label(self.emp_window, text="Balance", font="Aerial 12 bold")
        self.balancelabel.place(x=820, y=240)
        self.balance_ent = Entry(self.emp_window)
        self.balance_ent.place(x=800, y=280)

    def totalguds(self):
        amnt = self.totallabel
        for x in amnt:
            print(sum(x))

    def add_cart(self):

        proName = self.proName_ent.get()
        intprice = self.ent_price.get()
        intquantity = self.ent_quant.get()
        if intquantity =="":
            tkinter.messagebox.showerror("null", "fill quantity")
        else:

            price =int(intprice)
            quantity= int(intquantity)
            self.pro_frame = Frame(self.txtarea, height=27)
            self.pro_frame.pack(fill="x")
            self.pro_frame.config(bg="white")
            self.productName = Label(self.pro_frame, text=proName, font="Aerial 10 bold")
            self.productName.place(x=2, y=2)
            self.productName.config(bg="white")
            self.pricelabel = Label(self.pro_frame, text=price, font="Aerial 10 bold")
            self.pricelabel.place(x=110, y=2)
            self.pricelabel.config(bg="white")
            self.quantitylabel = Label(self.pro_frame, text=quantity, font="Aerial 10 bold")
            self.quantitylabel.place(x=200, y=2)
            self.quantitylabel.config(bg="white")
            self.totallabel = Label(self.pro_frame, text=price*quantity, font="Aerial 10 bold")
            self.totallabel.place(x=280, y=2)
            self.totallabel.config(bg="white")


    def search_pro(self):
        searchCode = self.search_code.get()
        if searchCode == "":
            tkinter.messagebox.showerror("error", "enter product code")
        try:
            mycur.execute("SELECT * FROM tbl_product WHERE productCode='"+searchCode+"'")
            myresult = mycur.fetchall()
            for x in myresult:
             self.proName_ent.delete(0, END)
             self.proName_ent.insert(END, x[1])
             self.ent_categ.delete(0, END)
             self.ent_categ.insert(END, x[2])
             self.ent_price.delete(0, END)
             self.ent_price.insert(END, x[3])
             self.quantAvailabel.delete(0, END)
             self.quantAvailabel.insert(END, x[4])

             return None

        except Exception:
            tkinter.messagebox.showerror("null", "product does not exist")
    def reset(self):
        self.search_code.delete(0, END)
        self.proName_ent.delete(0, END)
        self.ent_quant.delete(0, END)
        self.ent_price.delete(0, END)
        self.ent_categ.delete(0, END)
        self.quantAvailabel.delete(0, END)

    def run(self):
        self.emp_window.mainloop()

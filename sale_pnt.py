from tkinter import *
from sales_window import manager_window, employee


class sales:
    def __init__(self):
        self.pane = Tk()
        self.pane.geometry("300x300")
        self.label1 = Label(self.pane, text="Enter As :")
        self.label1.place(x=50, y=30)
        self.btn1 = Button(self.pane, text="Employee", font="times 12 bold", command=employee_ent)
        self.btn1.place(x=50, y=80)
        self.btn2 = Button(self.pane, text="Admin", font="times 12 bold", command=manager_ent)
        self.btn2.place(x=50, y=120)

    def run(self):
        self.pane.mainloop()


def manager_ent():
    root = manager_window()
    root.run()


def employee_ent():
    root = employee()
    root.run()


app = sales()
app.run()
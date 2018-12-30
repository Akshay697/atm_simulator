from display_page import Display
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from data_base import DBconnect

con = DBconnect()
root = Tk()
root.geometry('400x400+100+100')
root.title("Log in ")
Label(root, text="ATM No. : ").grid(row=5, column=2, padx=10, pady=10)
num = StringVar()
atm_num = Entry(root, textvariable=num)
atm_num.grid(row=5, column=5, padx=2, pady=2)
Label(root, text="Pin :").grid(row=8, column=2)
pin = StringVar()
atm_pin = Entry(root, textvariable=pin)
atm_pin.grid(row=8, column=5, padx=2, pady=2)


def submit():
    x = con.validate(num.get(), pin.get())
    if x:
        root.destroy()
        d = Display()
        d.geometry('400x400+100+100')

    else:
        messagebox.showerror("Error", "Wrong inputs")


Button(root, text="Submit", command=submit).grid(column=5, row=10)

root.mainloop()
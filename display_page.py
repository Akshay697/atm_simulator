from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from data_base import DBconnect
import tkinter as tk

con = DBconnect()
font = "Helvetica 16 bold"


class Display(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_rowconfigure(0,weight=1)

        self.frames = {}

        for f in (Window, Balance, Deposit, WithDrawl, PinChange):
            frame = f(container,self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="news")

        self.show_frame(Window)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class Window(tk.Frame):
    def __init__(self,master,controller):
        self.master = master
        tk.Frame.__init__(self, master)
        tk.Label(self,text="Welcome to ABC ATM",fg="blue",font = font).grid(row=0, column=4,padx=2,pady=2)
        name=con.getname()
        greet = "Welcome "+name
        tk.Label(self, text=greet,fg="red",bg="yellow",font=font).grid(row=2, column=4,padx=2,pady=2)
        Button(self,text = "Balance Enquiry", command=lambda: controller.show_frame(Balance)).grid(row=5, column=5, padx=2, pady=2)
        Button(self, text="Deposit", command=lambda : controller.show_frame(Deposit)).grid(row=7, column=5, padx=2, pady=2)
        Button(self,text="WithDrawl", command=lambda: controller.show_frame(WithDrawl)).grid(row=9, column=5, padx=2, pady=2)
        Button(self, text="Change Pin", command=lambda: controller.show_frame(PinChange)).grid(row=11, column=5, padx=2, pady=2)
        Button(self, text="Exit", command=self.master.quit).grid(row=15, column=3, padx=2, pady=2)


class Balance(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        bal = con.balance()
        Label(self, text=bal,font=font).grid(row=5, column=5,padx=2,pady=2)
        Button(self,text="cancel", command=self.master.quit).grid(row=7, column=5,padx=2,pady=2)
        Button(self,text="Back", command=lambda: controller.show_frame(Window)).grid(row=7, column=8,padx=2,pady=2)


class Deposit(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        Label(self, text="Enter Amount to be Deposit :",font=font).grid(row=2, column=4,padx=2,pady=2)
        amt = StringVar()
        Entry(self, textvariable=amt).grid(row=4, column=3,padx=2,pady=2)

        def submit():
            con.transaction(amt.get(), 'deposit')

        Button(self, text="deposit", command=submit).grid(row=6, column=3,padx=2,pady=2)
        Button(self, text="Cancel", command=self.master.quit).grid(row=6, column=1,padx=2,pady=2)


class WithDrawl(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        Label(self, text="Enter Amount to be Withdrawl :",font=font).grid(row = 6, column=3,padx=2,pady=2)
        amt = StringVar()
        Entry(self, textvariable=amt).grid(row=8,column=3,padx=2,pady=2)

        def submit():
            con.transaction(amt.get(), 'withdrawl')

        Button(self,text="withdrawl", command=submit).grid(row = 10, column=3,padx=2,pady=2)
        Button(self, text="Cancel", command=self.master.quit).grid(row=10, column=1,padx=2,pady=2)


class PinChange(tk.Frame):
    def __init__(self,master,controller):
        tk.Frame.__init__(self, master)
        self.master = master
        Label(self,text="Change Pin ",font=font).grid(row=0, column=4,padx=2,pady=2)
        Label(self, text="Enter Current Pin").grid(row=2, column=3,padx=2,pady=2)
        c_pin = StringVar()
        Entry(self, textvariable=c_pin,).grid(row=3, column=3,padx=2,pady=2)
        Label(self,text="Enter New Pin").grid(row=5, column=3,padx=2,pady=2)
        n_pin = StringVar()
        Entry(self, textvariable=n_pin).grid(row=6, column=3,padx=2,pady=2)
        c_n_pin = StringVar()
        Label(self, text="Confirm New Pin").grid(row=8, column=3,padx=2,pady=2)
        Entry(self, textvariable=c_n_pin).grid(row=9, column=3,padx=2,pady=2)

        def changepin():
            if n_pin.get() == c_n_pin.get():
                x = con.pinchange(c_pin.get(), n_pin.get())
                if x:
                    messagebox.showinfo("Pin Change", "Pin change Successfully")

                else:
                    messagebox.showerror("Error","Current Pin is wrong")
            else:
                messagebox.showerror("Error", "New Pin didn't match ")
        Button(self, text="Change Pin", command=changepin).grid(row=10, column=5,padx=2,pady=2)
        Button(self, text="cancel", command=lambda: controller.show_frame(Window))

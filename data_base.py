import pymysql as py
from tkinter import messagebox


atm_num = ""
atm_pin = ""
class DBconnect:
    def __init__(self):
        try:
            self.db = py.connect("localhost","root","akshay8287","customers_details")

        except RuntimeError:
            messagebox.showerror("Error","Database is not Present")

    def validate(self,num,pin):
        cursor = self.db.cursor()
        global atm_num
        global atm_pin
        atm_pin = pin
        atm_num = num
        print("this is number : ",num)
        try:
            sql = "select * from atm_details where atm_num='"+num+"'"
            cursor.execute(sql)
            rs = cursor.fetchall()
            for row in rs:
                a_num = row[0]
                a_pin = row[1]

            cursor.close()
            print("this is row affected", cursor.rowcount)

            print(a_num)
            print(a_pin)
            if num == a_num and pin == a_pin:
                return True
            else:
                return False
        except:
            messagebox.showerror("Error", "ATM number or Pin is invalid")

    def getname(self):
        cursor = self.db.cursor()
        sql = "select * from atm_details where atm_num='"+atm_num+"'"
        cursor.execute(sql)
        rs = cursor.fetchall()
        for r in rs:
            name = r[2]
        return name

    def balance(self):

        cursor = self.db.cursor()
        sql = "select * from atm_details where atm_num='"+atm_num+"'"
        cursor.execute(sql)
        rs = cursor.fetchall()
        for r in rs:
            balance = r[4]

        cursor.close()
        print(balance)
        return balance

    def transaction(self,amt,choice):

        cursor = self.db.cursor()
        sql = "Select * from atm_details where atm_num='"+atm_num+"'"
        cursor.execute(sql)
        rs = cursor.fetchall()
        for r in rs:
            balance = r[4]

        n_amt = int(amt)
        n_balance = int(balance)
        if choice == 'deposit':
            n_total = n_amt + n_balance
        elif choice == 'withdrawl':
            if n_amt > n_balance:
                messagebox.showerror("Error","Insufficient Balance")
            else:
                n_total = n_balance-n_amt

        total = str(n_total)
        sql = "UPDATE atm_details SET balance=%s WHERE atm_num=%s"
        val = (total, atm_num)
        cursor.execute(sql, val)
        self.db.commit()

    def pinchange(self, c_pin, n_pin):
        if c_pin == atm_pin:
            cursor = self.db.cursor()
            sql = "Update atm_details set atm_pin=%s where atm_num=%s"
            val = (n_pin, atm_num)
            cursor.execute(sql, val)
            self.db.commit()
            return True
        else:
            return False







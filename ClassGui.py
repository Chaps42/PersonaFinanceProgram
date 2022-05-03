import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser

import FileTypes as ft
import Windows as win
import UIElements as ui

class MainGui:

    def __init__(self,master):
        self.master = master
        self.Profile = ft.Profile("Emptyyy","Password","/Users/DavidChaparro/Desktop/Personal Projects/PersonaFinanceProgram")

        ####Initialize Master Frame for all pages#####
        self.frame =  ttk.Notebook(self.master)
        self.p1 = ttk.Frame(self.frame)
        self.p2 = ttk.Frame(self.frame)
        self.p3 = ttk.Frame(self.frame)
        self.p4 = ttk.Frame(self.frame)
        self.p5 = ttk.Frame(self.frame)
        self.p6 = ttk.Frame(self.frame)
        self.p7 = ttk.Frame(self.frame)
        self.p8 = ttk.Frame(self.frame)
        self.p9 = ttk.Frame(self.frame)
        self.frame.add(self.p1, text = "Overview")
        self.frame.add(self.p2, text = "Income")
        self.frame.add(self.p3, text = "Expenses")
        self.frame.add(self.p4, text = "Groupings")
        self.frame.add(self.p5, text = "Vacations")
        self.frame.add(self.p6, text = "Accounts Over Time")
        self.frame.add(self.p7, text = "Graphs")
        self.frame.add(self.p8, text = "Reccuring Transactions")
        self.frame.add(self.p9, text = "Records")

        #####Page 1#####
        ttk.Label(self.p1, text = "Account Overview").grid(column = 0, row = 0, sticky = 'w')
        ttk.Label(self.p1, text = "Current Profile: "+self.Profile.name).grid(column = 1, row = 0, sticky = 'w')
        ttk.Button(self.p1, text = "New Profile",command = self.New_Profile).grid(column = 0, row = 1)
        ttk.Button(self.p1, text = "Load Profile",command = self.Load_Profile).grid(column = 0, row = 2)
        ttk.Button(self.p1, text = "Save",command = self.BKSave).grid(column = 5, row = 5)
        self.Utilization = ttk.Frame(self.p1)
        self.ExpChart = ttk.Frame(self.p1)

        self.Acc = ttk.Button(self.p1, text = "Test",command = self.test).grid(column = 5, row = 6)

        #Initialize account list here
        ACCLIST = ui.AccountList(self.p1,self.Profile.accounts,self.New_Account,self.Del_Account,self.BKRecAcc)

        self.Utilization.grid(column = 0, row = 4, rowspan = 2)
        ACCLIST.Acc.grid(column = 2, row = 4, rowspan = 2)
        self.ExpChart.grid(column = 4, row = 4, rowspan = 2)


        #####Page 2#####
        self.PieChartIncome = ttk.Frame(self.p2)

        IncomeTable = ui.IncExpGrid(self.p2,"Income",self.Profile.incexpcat,self.New_IncExp,self.Del_IncExp,self.BKRecIncExp)
        IncomeTable.IEGrid.grid(row = 0,column = 0, sticky = 'nsew')
        self.PieChartIncome.grid(row = 0, column = 1)

        #####Page 3#####
        self.PieChartExpenses = ttk.Frame(self.p3)

        ExpenseTable = ui.IncExpGrid(self.p3,"Expense",self.Profile.incexpcat,self.New_IncExp,self.Del_IncExp,self.BKRecIncExp)
        ExpenseTable.IEGrid.grid(row = 0,column = 0, sticky = 'nsew')
        self.PieChartExpenses.grid(row = 0, column = 1)

        #####Page 4#####
        self.TimeChart = ttk.Frame(self.p4)
        ttk.Label(self.p4, text = "Accounts Over Time").grid(row = 0, column = 0)
        ttk.Button(self.p4, text = "Record Current Values").grid(row = 0, column = 1)

        self.AccountTable = ttk.Treeview(self.p4,columns = self.columns)

        self.AccountTable.heading("1", text = "Type 1")
        self.AccountTable.heading("2", text = "Type 2")
        self.AccountTable.heading("3", text = "Type 3")

        self.AccountTable.grid(row = 1,column = 0, sticky = 'nse')
        self.TimeChart.grid(row = 1, column = 1)

        #####Page 5#####

        #####Page 6#####
        ttk.Label(self.p6, text = "Recurring Transactions").grid(row = 0, column = 0, sticky = 'w')

        self.G = ttk.Frame(self.p6)
        ttk.Label(self.G,text = "Recurring Income").grid(row = 0, column = 0, sticky = 'w')
        ttk.Label(self.G,text = "Recurring Expenses").grid(row = 0, column = 3, sticky = 'w')
        ttk.Button(self.G, text = "New Recurring Transaction").grid(row = 0, column = 5)

        self.G.grid(row = 1, column = 0, rowspan = 6)

        #####Page 7#####
        ttk.Label(self.p7, text = "Records: ").grid(row = 0, column = 0, sticky = 'w')
        self.RecordSheet = tk.Text(self.p7)


        self.RecordSheet.grid(row = 1, column = 0)
        #.grid all items to make them real
        self.frame.grid()


    #####New Window Functions#####
    def New_Profile(self): #CHECK#
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("New Profile")
        self.app = win.WinNewProfile(self.NewWindow,self.BKOverwrite_Profile)

    def Load_Profile(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("Load Profile")
        self.app = win.WinLoadProfile(self.NewWindow,self.BKOverwrite_Profile)

    def New_Account(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("New Account Details")
        self.app = win.WinNewAccount(self.NewWindow,self.BKNew_Acc)

    def Del_Account(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("New Account Details")
        self.app = win.WinDelAccount(self.NewWindow,self.Profile.accounts,self.BKDel_Acc)

    def New_IncExp(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("New Income/Expense")
        self.app = win.WinNewIncExp(self.NewWindow,self.BKNewIncExp)

    def Del_IncExp(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("New Income")
        self.app = win.WinDelIncExp(self.NewWindow)

    #####PassBack Functions#####

    def BKOverwrite_Profile(self,NewProfile):
        self.Profile = NewProfile
        print("New Profile Created")

    def BKNewIncExp(self,name,Type,Color):
        self.Profile.New_IncExp_Catagory(name,Type,Color)
        print("New Catagory Created")
        IncomeTable.IEGrid.destroy()
        ExpenseTable.IEGrid.destroy()
        IncomeTable = ui.IncExpGrid(self.p2,"Income",self.Profile.incexpcat,self.New_IncExp,self.Del_IncExp,self.BKRecIncExp)
        IncomeTable.IEGrid.grid(row = 0,column = 0, sticky = 'nsew')
        ExpenseTable = ui.IncExpGrid(self.p3,"Expense",self.Profile.incexpcat,self.New_IncExp,self.Del_IncExp,self.BKRecIncExp)
        ExpenseTable.IEGrid.grid(row = 0,column = 0, sticky = 'nsew')

    def BKDelIncExp(self,name):
        self.Profile.Del_IncExp_Catagory(name)
        print("Catagory Deleted")
        IncomeTable.IEGrid.destroy()
        ExpenseTable.IEGrid.destroy()
        IncomeTable = ui.IncExpGrid(self.p2,"Income",self.Profile.incexpcat,self.New_IncExp,self.Del_IncExp,self.BKRecIncExp)
        IncomeTable.IEGrid.grid(row = 0,column = 0, sticky = 'nsew')
        ExpenseTable = ui.IncExpGrid(self.p3,"Expense",self.Profile.incexpcat,self.New_IncExp,self.Del_IncExp,self.BKRecIncExp)
        ExpenseTable.IEGrid.grid(row = 0,column = 0, sticky = 'nsew')

    def BKRecIncExp(self):
        print("HI")

    def BKNew_Acc(self,name,Type,Color):
        self.Profile.New_Account(name,Type,Color)
        print("New Account created")
        ACCLIST.Acc.destroy()
        ACCLIST = ui.AccountList(self.p1,self.Profile.accounts,self.New_Account,self.Del_Account,self.BKRecAcc)
        ACCLIST.Acc.grid(column = 2, row = 4, rowspan = 2)

    def BKDel_Acc(self,name):
        self.Profile.Delete_Account(name)
        print(" Account deleted")
        ACCLIST.Acc.destroy()
        ACCLIST = ui.AccountList(self.p1,self.Profile.accounts,self.New_Account,self.Del_Account)
        ACCLIST.Acc.grid(column = 2, row = 4, rowspan = 2)

    def BKRecAcc(self):
        print("Bruh")

    def BKSave(self):
        self.Profile.Save_Profile(self.Profile.directory)


    def test(self):
        print(self.Profile.accounts)



def main():
    root = tk.Tk()
    app = MainGui(root)
    root.mainloop()

if __name__ == '__main__':
    main()

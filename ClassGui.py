import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser

import FileTypes as ft

class MainGui:

    def __init__(self,master):
        self.master = master
        self.Profile = ft.Profile("Emptyyy","Password")

        ####Initialize Master Frame for all pages#####
        self.frame =  ttk.Notebook(self.master)
        self.p1 = ttk.Frame(self.frame)
        self.p2 = ttk.Frame(self.frame)
        self.p3 = ttk.Frame(self.frame)
        self.p4 = ttk.Frame(self.frame)
        self.p5 = ttk.Frame(self.frame)
        self.p6 = ttk.Frame(self.frame)
        self.p7 = ttk.Frame(self.frame)
        self.frame.add(self.p1, text = "Overview")
        self.frame.add(self.p2, text = "Income")
        self.frame.add(self.p3, text = "Expenses")
        self.frame.add(self.p4, text = "Accounts Over Time")
        self.frame.add(self.p5, text = "Graphs")
        self.frame.add(self.p6, text = "Reccuring Transactions")
        self.frame.add(self.p7, text = "Records")

        #Test Values
        self.Accounts = ["Account A", "Account B", "Account C"]
        self.Debts = ["Debt A", "Debt B", "Debt C"]
        self.Expenses = ["Expense A","Expense B","Expense C"]
        self.Incomes = ["Income A", "Income B", "Income C"]
        self.columns = ["1","2","3","4"]

        #####Page 1#####
        ttk.Label(self.p1, text = "Account Overview").grid(column = 0, row = 0, sticky = 'w')
        ttk.Button(self.p1, text = "New Profile",command = self.New_Profile).grid(column = 0, row = 1)
        ttk.Button(self.p1, text = "Load Profile",command = self.Load_Profile).grid(column = 0, row = 2)
        ttk.Button(self.p1, text = "Record Account Values").grid(column = 5, row = 2)
        ttk.Button(self.p1, text = "Save").grid(column = 5, row = 5)
        ttk.Label(self.p1, text = "Date:").grid(column = 4, row = 1)
        ttk.Entry(self.p1).grid(column = 5, row = 1)
        self.Utilization = ttk.Frame(self.p1)
        self.Acc = ttk.Frame(self.p1)
        self.ExpChart = ttk.Frame(self.p1)

        ttk.Button(self.p1, text = "Test",command = self.test).grid(column = 5, row = 6)
        
        ttk.Label(self.Acc, text = "Accounts").grid(row = 0, column = 0,sticky = 'w')
        ttk.Button(self.Acc, text = "New Account",command = self.New_Account).grid(row = 0, column = 1)
        ttk.Label(self.Acc, text = "Assets").grid(row = 1, column = 0,sticky = 'w')
        ttk.Label(self.Acc, text = "Debts").grid(row = 1, column = 1,sticky = 'w')
        for i in range(len(self.Accounts)):
            ttk.Label(self.Acc, text = self.Accounts[i]).grid(row = 2+2*i, column = 0,sticky = 'w')
            ttk.Entry(self.Acc).grid(row = 3+2*i, column = 0)
        for i in range(len(self.Debts)):
            ttk.Label(self.Acc, text = self.Debts[i]).grid(row = 2+2*i, column = 1,sticky = 'w')
            ttk.Entry(self.Acc).grid(row = 3+2*i, column = 1)

        self.Utilization.grid(column = 0, row = 4, rowspan = 2)
        self.Acc.grid(column = 2, row = 4, rowspan = 2)
        self.ExpChart.grid(column = 4, row = 4, rowspan = 2)
    

        #####Page 2#####
                                                                    
        self.PieChartIncome = ttk.Frame(self.p2) 
        ttk.Label(self.p2, text = "Income").grid(row = 0, column = 0, sticky = 'w')
        ttk.Button(self.p2, text = "New Entry",command = self.New_IncExp).grid(row = 0, column = 1)
        text = ttk.Entry(self.p2).grid(row =1 , column = 0)
        
        self.ExpenseTable = ttk.Treeview(self.p2,columns = self.columns)
        self.ExpenseTable.heading("1", text = "Type 1")
        self.ExpenseTable.heading("2", text = "Type 2")
        self.ExpenseTable.heading("3", text = "Type 3")

        self.ExpenseTable.grid(row = 2,column = 0, sticky = 'nsew')
        self.PieChartIncome.grid(row = 2, column = 1) 

        #####Page 3#####
        self.PieChartExpenses = ttk.Frame(self.p3)
        ttk.Label(self.p3, text = "Expenses").grid(row = 0, column = 0,sticky = 'w')
        ttk.Button(self.p3, text = "New Entry",command = self.New_IncExp).grid(row = 0, column = 1)

        self.IncomeTable = ttk.Treeview(self.p3,columns = self.columns)
        self.IncomeTable.heading("1", text = "Type 1")
        self.IncomeTable.heading("2", text = "Type 2")
        self.IncomeTable.heading("3", text = "Type 3")

        self.IncomeTable.grid(row = 1,column = 0, sticky = 'nse')
        self.PieChartIncome.grid(row = 2, column = 1)

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
        
    def Update_Profile(self):
        self.Profile = self.app.Profile
        #self.Update_Profile()


    #####New Window Functions#####
    def New_Profile(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("New Profile")
        self.app = NewProfile(self.NewWindow,self)
        print("HI1")

    def Load_Profile(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("Load Profile")
        self.app = LoadProfile(self.NewWindow)

    def New_Account(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("New Account Details")
        self.app = NewAccount(self.NewWindow)

    def New_IncExp(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("New Income/Expense")
        self.app = NewIncExp(self.NewWindow)

    def Del_IncExp(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.NewWindow.title("New Income")
        self.app = NewIncome(self.NewWindow)

    def test(self):
        print(self.app.Profile.name)
        print(self.app.master)


#New Window Classes
        
class NewProfile:
    def __init__(self,master,main):
        self.master = master
        print("Hi2")


        #Initialize values for accounts
        self.Profile = ft.Profile("EmptyInClass","Password")
        self.Name = tk.StringVar()
        self.Password = tk.StringVar()
        self.PasswordConfirm = tk.StringVar()
        self.FileDirectory = tk.StringVar()
        
        self.t = ttk.Frame(self.master)
        #Name, Location, Password
        ttk.Label(self.t, text = "Name: ").grid(row = 2, column = 0)
        ttk.Label(self.t, text = "Password:").grid(row = 3, column = 0)
        ttk.Label(self.t, text = "Confirm Password:").grid(row = 4, column = 0)
        ttk.Label(self.t, text = "File Directory:").grid(row = 5, column = 0)
        ttk.Entry(self.t,textvariable = self.Name).grid(row = 2, column = 1,columnspan = 2)
        ttk.Entry(self.t,textvariable = self.Password).grid(row = 3, column = 1,columnspan = 2)
        ttk.Entry(self.t,textvariable = self.PasswordConfirm).grid(row = 4, column = 1,columnspan = 2)
        ttk.Entry(self.t,textvariable = self.FileDirectory).grid(row = 5, column = 1,columnspan = 2)

        #Continue and save new profile
        ttk.Button(self.t, text = "Continue", command = self.New_Profile).grid(row = 6, column =  2)
        ttk.Button(self.t, text = "Cancel", command = self.master.destroy).grid(row = 6, column = 1)
        self.t.grid()

    def New_Profile(self):
        if self.Password.get() == self.PasswordConfirm.get():
            self.Profile = ft.Profile(self.Name.get(),self.Password.get())
            self.Profile.Save_Profile(self.FileDirectory.get())
            self.master.destroy()
            print("Hi3")
            
        if self.Password.get() != self.PasswordConfirm.get():
            ttk.Label(self.t,text = "Passwords do not match", foreground='red').grid(row = 6,column = 1)


    
class LoadProfile:
    def __init__(self,master):
        self.master = master
        
        self.filename = tk.filedialog.askopenfilename()

        self.t = ttk.Frame(self.master)
        ttk.Label(self.t, text = "Password").grid(row = 0, column = 0)
        ttk.Entry(self.t).grid(row = 0, column = 1)
        ttk.Button(self.t, text = "Continue", command = self.master.destroy).grid(row = 0, column =  2)
        self.t.grid()

class NewAccount:
    def __init__(self,master):
        self.master = master
        self.AType = tk.StringVar(self.master,"Credit")

        self.t = ttk.Frame(self.master)
        ttk.Label(self.t, text = "Account Name:").grid(row = 0, column = 0)
        ttk.Entry(self.t).grid(row = 0, column = 1)
        ttk.Label(self.t, text = "Account Type:").grid(row = 1, column = 0)
        ttk.Radiobutton(self.t,text = "Credit", variable = self.AType, value = "Credit", command = lambda:P(AType)).grid(row = 2, column = 0)
        ttk.Radiobutton(self.t,text = "Debt", variable = self.AType, value = "Debt", command = lambda:P(AType)).grid(row = 2, column = 1)
        ttk.Button(self.t, text = "Continue", command = self.master.destroy).grid(row = 3, column =  2)
        self.t.grid()

class NewIncExp:
    def __init__(self,master):
        self.master = master
        self.t = ttk.Frame(self.master)

        self.Name = tk.StringVar()
        self.Color = tk.StringVar()
        self.Type = tk.StringVar(value = 'Asset')

        self.values = {"RadioButton 1":'Asset', "RadioButton 2":'Debt'}
        
        ttk.Label(self.t, text = "Catagory Name:").grid(row = 0, column = 0)
        ttk.Entry(self.t,textvariable = self.Name).grid(row = 0, column = 1,columnspan = 2)

        self.AType = tk.StringVar(self.master,"Credit")
        ttk.Label(self.t, text = "Type:").grid(row = 1, column = 0)
        ttk.Radiobutton(self.t,text = "Asset", variable = self.Type, value = "Asset").grid(row = 1, column = 1)
        ttk.Radiobutton(self.t,text = "Debt", variable = self.Type, value = "Debt").grid(row = 1, column = 2)
        clr = '#aa0120'
        ttk.Label(self.t, text = "Color").grid(row = 3, column = 0)
        ttk.Button(self.t,command = lambda: colorchooser.askcolor(initialcolor=clr)).grid(row = 3, column = 1,columnspan = 2)
        
        
        ttk.Button(self.t, text = "Continue", command = self.New_Catagory).grid(row = 4, column =  2)
        self.t.grid()

    def New_Catagory(self):
        ft.IncExpCatagory(self.Name.get(),self.Type.get(),self.Color.get())
        self.master.destroy()
        

def main():
    root = tk.Tk()
    app = MainGui(root)
    root.mainloop()

if __name__ == '__main__':
    main()

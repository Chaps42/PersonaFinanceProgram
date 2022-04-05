import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser

import FileTypes as ft

#New Window Classes
        
class WinNewProfile:
    def __init__(self,master,update):
        self.master = master
        self.update = update

        #Initialize values for accounts
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
            self.Profile = ft.Profile(self.Name.get(),self.Password.get(),self.FileDirectory.get())
            self.Profile.Save_Profile(self.FileDirectory.get())
            self.update(self.Profile)
            self.master.destroy()
            
        if self.Password.get() != self.PasswordConfirm.get():
            ttk.Label(self.t,text = "Passwords do not match", foreground='red').grid(row = 6,column = 1)
            

    
class WinLoadProfile:
    def __init__(self,master,update):
        self.master = master
        self.update = update
        
        self.filename = tk.filedialog.askopenfilename() #Ask for filename
        self.t = ttk.Frame(self.master)
        ttk.Label(self.t, text = "Password").grid(row = 0, column = 0)
        ttk.Entry(self.t).grid(row = 0, column = 1)
        ttk.Button(self.t, text = "Continue", command = self.Load_Profile).grid(row = 0, column =  2)
        self.t.grid()


class WinNewAccount:
    def __init__(self,master,func):
        self.master = master
        self.func = func

        self.Name = tk.StringVar()
        self.Color = tk.StringVar()
        self.Type = tk.StringVar(value = 'Asset')

        self.values = {"RadioButton 1":'Asset', "RadioButton 2":'Debt'}

        self.t = ttk.Frame(self.master)
        ttk.Label(self.t, text = "Account Name:").grid(row = 0, column = 0)
        ttk.Entry(self.t,textvariable = self.Name).grid(row = 0, column = 1)
        ttk.Label(self.t, text = "Account Type:").grid(row = 1, column = 0)
        ttk.Radiobutton(self.t,text = "Asset", variable = self.Type, value = "Asset").grid(row = 1, column = 1)
        ttk.Radiobutton(self.t,text = "Debt", variable = self.Type, value = "Debt").grid(row = 1, column = 2)
        ttk.Button(self.t, text = "Continue", command = self.New_Account).grid(row = 3, column =  2)
        ttk.Button(self.t, text = "Cancel", command = self.master.destroy).grid(row = 3, column = 1)
        self.t.grid()

    def New_Account(self):
        self.func(self.Name.get(),self.Type.get(),self.Color.get())
        self.master.destroy()

class WinDelAccount:
    def __init__(self,master,accounts,function):
        self.master = master
        self.func = function
        self.list = list(accounts.keys())

        self.t = ttk.Frame(self.master)
        ttk.Label(self.t, text = "Choose an Account to Delete:").grid(row = 0, column = 0,columnspan = 2)
        #insert menu pull down here
        ttk.Button(self.t, text = "Continue", command = self.Del_Account).grid(row = 2, column =  1)
        ttk.Button(self.t, text = "Cancel", command = self.master.destroy).grid(row = 2, column = 0)
        self.t.grid()
        
    def Del_Account(self):
        print("Deleted Account")
        self.master.destroy()

class WinNewIncExp:
    def __init__(self,master,newinc):
        self.master = master
        self.t = ttk.Frame(self.master)
        self.newinc = newinc

        self.Name = tk.StringVar()
        self.Color = tk.StringVar()
        self.Type = tk.StringVar(value = 'Asset')

        self.values = {"RadioButton 1":'Income', "RadioButton 2":'Expense'}
        
        ttk.Label(self.t, text = "Catagory Name:").grid(row = 0, column = 0)
        ttk.Entry(self.t,textvariable = self.Name).grid(row = 0, column = 1,columnspan = 2)

        self.AType = tk.StringVar(self.master,"Credit")
        ttk.Label(self.t, text = "Type:").grid(row = 1, column = 0)
        ttk.Radiobutton(self.t,text = "Income", variable = self.Type, value = "Asset").grid(row = 1, column = 1)
        ttk.Radiobutton(self.t,text = "Expense", variable = self.Type, value = "Debt").grid(row = 1, column = 2)
        ttk.Label(self.t, text = "Color").grid(row = 3, column = 0)
        ttk.Button(self.t,command = lambda: colorchooser.askcolor(initialcolor=clr)).grid(row = 3, column = 1,columnspan = 2)
        
        
        ttk.Button(self.t, text = "Continue", command = self.New_Catagory).grid(row = 4, column =  2)
        ttk.Button(self.t, text = "Cancel", command = self.master.destroy).grid(row = 4, column = 1)
        
        self.t.grid()

    def New_Catagory(self):
        self.newinc(self.Name.get(),self.Type.get(),self.Color.get())
        self.master.destroy()

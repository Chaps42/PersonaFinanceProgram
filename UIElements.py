import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser

import FileTypes as ft

##### UI Elements #####

##class SpreadSheet:
class AccountList:
    def __init__(self,master,Accounts,NewACCCom,DelACCCom,RecCom):
        self.master = master
        self.Acc = ttk.Frame(self.master)
        LengthA = 0
        LengthD = 0
        
        date = tk.StringVar()

        #Test Values
        self.Accounts = list(Accounts.keys())

        ttk.Label(self.Acc, text = "Accounts").grid(row = 0, column = 0,sticky = 'w')

        ttk.Label(self.Acc, text = "Date:").grid(column = 0, row = 1,sticky = 'w')
        ttk.Entry(self.Acc).grid(column = 1, row = 1,sticky = 'w')
        ttk.Button(self.Acc, text = "Record Account Values",command = RecCom).grid(column = 2, row = 1)
        
        ttk.Button(self.Acc, text = "New Account",command = NewACCCom).grid(row = 2, column = 0)
        ttk.Button(self.Acc, text = "Delete Account",command = DelACCCom).grid(row = 2, column = 1)
        ttk.Label(self.Acc, text = "Assets").grid(row = 3, column = 0,sticky = 'w')
        ttk.Label(self.Acc, text = "Debts").grid(row = 3, column = 2,sticky = 'w')
        for i in range(len(self.Accounts)):
            if Accounts[self.Accounts[i]].type == 'Asset':
                ttk.Label(self.Acc, text = self.Accounts[i]).grid(row = 4+2*LengthA, column = 0,sticky = 'w',columnspan = 1)
                ttk.Entry(self.Acc,).grid(row = 5+2*LengthA, column = 0,columnspan = 1)
                LengthA += 2
            if Accounts[self.Accounts[i]].type == 'Debt':
                ttk.Label(self.Acc, text = self.Accounts[i]).grid(row = 4+2*LengthD, column = 1,sticky = 'w',columnspan = 1)
                ttk.Entry(self.Acc).grid(row = 5+2*LengthD, column = 1,columnspan = 1)
                LengthD += 2

class IncExpGrid:
    def __init__(self,master,Type,IncExps,NewCat,DeleteCat,RecordVal)
        self.Cats = list(IncExps.keys())

        Dates = []
        Cats = []
        
        for names in self.Cats:
            if IncExps[names].type == Type
                Cats.append(names)
                TempDs = list(IncExps[names].values.keys()) #Could append directly to library
                for i in range(len(TempDs)): #And Remove duplicates somehow easily
                    if TempDs[i] not in Dates:
                        Dates.append(TempDs[i])

        Grid = [len(Cats)+2,len(Dates)+1]
        GridVal = [[tk.StringVar()for j in range(len(Cats)+2)]for i in range(len(Dates))]

        self.master = master
        self.IEGrid = ttk.Frame(self.master)

        ttk.Label(self.IEGrid, text = "Income").grid(row = 0, column = 0, sticky = 'w')
        ttk.Button(self.IEGrid, text = "New Entry",command = self.New_IncExp).grid(row = 0, column = 1)
        ttk.Entry(self.IEGrid).grid(row =1 , column = 0)

        ttk.Label(self.IEGrid,text = "Dates")
        ttk.Label(self.IEGrid,text = "Total")

        RS = 2

        Grid[0,0] = ttk.Label(self.IEGrid,text = "Dates").grid(row = RS, column = 0)
        Grid[-1,0] = ttk.Label(self.IEGrid,text = "Total").grid(row = RS, column = len(Cats)+1)
        for i in range(len(Cats)):
            Grid[i+1,0] = ttk.Label(self.IEGrid,text = Cats[i]).grid(row = RS, column = i+1)
            for j in range(len(Dates)):
                ttk.Entry(self.IEGrid,variable = GridVal[j][i]).grid(row = RS+j+1,column = i+1)
                
            
        
            
            

        
        
    



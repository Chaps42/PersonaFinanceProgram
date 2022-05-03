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
        ttk.Label(self.Acc, text = "Debts").grid(row = 3, column = 1,sticky = 'w')
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
    def __init__(self,master,Type,IncExps,NewCat,DeleteCat,RecordVal,NewDate):
        self.Cats = list(IncExps.keys())
        self.IEGrid = ttk.Frame(master)

        Dates = []
        Cats = []

        NewDate = tk.StringVar()

        for names in self.Cats:
            if IncExps[names].type == Type:
                print(IncExps[names].type)
                Cats.append(names)
                TempDs = list(IncExps[names].values.keys()) #Could append directly to library
                for i in range(len(TempDs)): #And Remove duplicates somehow easily
                    if TempDs[i] not in Dates:
                        Dates.append(TempDs[i]) #List of all catagories and dates

        ttk.Label(self.IEGrid, text = Type).grid(row = 0, column = 0, sticky = 'w')
        ttk.Button(self.IEGrid, text = "New Entry Date",command = NewDate).grid(row = 1, column = 0)
        ttk.Entry(self.IEGrid,textvariable = NewDate).grid(row =1 , column = 1)
        ttk.Button(self.IEGrid, text = "Record Values: ",command = RecordVal).grid(row = 1, column = 6)
        ttk.Button(self.IEGrid, text = "New Catagory",command = NewCat).grid(row = 1, column = 4)
        ttk.Button(self.IEGrid, text = "Delete Catagory",command = DeleteCat).grid(row = 1, column = 5)

        #Start of main grid of expenses
        h=tk.Scrollbar(self.IEGrid, orient='horizontal')

        RS = 2

        #Create grid to use  #GridVal[row][column]
        GridVal = [[tk.StringVar() for j in range(len(Cats)+2)]for i in range(len(Dates))]
        Grid = [[ttk.Entry(self.IEGrid,textvariable = GridVal[i][j]) for j in range(len(Cats)+2)]for i in range(len(Dates))]
        height = len(Dates)+1
        width = len(Cats)+2

        for i in range(width): #Columns
            for j in range(height): #Rows
                if j == 0:
                    if i ==0:
                        ttk.Label(self.IEGrid,text = "Dates").grid(row = RS+j, column = 0)
                    if i == width-1:
                        ttk.Label(self.IEGrid,text = "Total").grid(row = RS+j, column = len(Cats)+1)
                    if len(Cats)!=0 and i != width-1 and i != 0:
                        ttk.Label(self.IEGrid,text = Cats[i-1]).grid(row = RS+j, column = i)
                if j != 0:
                    if i == 0:
                        GridVal[j][i] = 10.0
                        Grid[j][i].grid(row = RS+j,column = i)
                    if i == width-1:
                        GridVal[j][i] = 11.0
                        Grid[j][i].grid(row = RS+j,column = i)
                    if len(Cats)!=0 and i != width-1 and i != 0:
                        GridVal[j][i] = 12.0
                        Grid[j][i].grid(row = RS+j,column = i)


        #h.config(command=text.xview)     
        #h.pack(side='bottom', fill='x')
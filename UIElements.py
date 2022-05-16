import tkinter as tk
import datetime as dt
from tkinter import Variable, ttk
from tkinter import filedialog
from tkinter import colorchooser
import
from sys import platform as OS 
import FileTypes as ft
from matplotlib.figure import Figure as Fig
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)


##### UI Elements #####

##class SpreadSheet:
class AccountList:
    def __init__(self,master,Accounts,NewACCCom,DelACCCom,RecCom,prevdate):
        self.master = master
        self.Acc = ttk.Frame(self.master)
        self.RecCom = RecCom
        LengthA = 0
        LengthD = 0
        
        self.prevdate = prevdate

        #Test Values
        self.ACKeys = list(Accounts.keys())
        self.Accs = Accounts

        #Find Most recent date
        tempdates = []
        for i in range(len(self.ACKeys)):
            for j in self.Accs[self.ACKeys[i]].dates:
                if j not in tempdates:
                    tempdates.append(j)
        now = dt.date.today()


        try:
            tempdates.sort(reverse=True)
            newest = tempdates[0]
            if newest < str(now): self.date = tk.StringVar(value = newest)
            if str(prevdate) != newest: self.date = tk.StringVar(value = prevdate)
        except ValueError: self.date = tk.StringVar(value = prevdate)
        except IndexError: self.date = tk.StringVar(value = prevdate)

        ttk.Label(self.Acc, text = "Accounts").grid(row = 0, column = 0,sticky = 'w')

        ttk.Label(self.Acc, text = "Date:").grid(column = 0, row = 1,sticky = 'w')
        ttk.Entry(self.Acc,textvariable=self.date).grid(column = 1, row = 1,sticky = 'w')
        ttk.Button(self.Acc, text = "Record Account Values",command = self.RecordAccounts).grid(column = 2, row = 1)
        
        ttk.Button(self.Acc, text = "New Account",command = NewACCCom).grid(row = 2, column = 0)
        ttk.Button(self.Acc, text = "Delete Account",command = DelACCCom).grid(row = 2, column = 1)
        ttk.Label(self.Acc, text = "Assets").grid(row = 3, column = 0,sticky = 'w')
        ttk.Label(self.Acc, text = "Debts").grid(row = 3, column = 1,sticky = 'w')
            

        self.AccVars = [tk.StringVar(value =  "0") for i in range(len(self.ACKeys))]
        for i in range(len(self.ACKeys)):
            if self.Accs[self.ACKeys[i]].type == 'Asset':
                try: self.AccVars[i] = tk.StringVar(value = self.Accs[self.ACKeys[i]].values[newest])
                except: self.AccVars[i] = tk.StringVar(value = "0")
                ttk.Label(self.Acc, text = self.ACKeys[i]).grid(row = 4+2*LengthA, column = 0,sticky = 'w',columnspan = 1)
                ttk.Entry(self.Acc,textvariable=self.AccVars[i]).grid(row = 5+2*LengthA, column = 0,columnspan = 1)
                LengthA += 2
            if self.Accs[self.ACKeys[i]].type == 'Debt':
                try: self.AccVars[i] = tk.StringVar(value = self.Accs[self.ACKeys[i]].values[newest])
                except: self.AccVars[i] = tk.StringVar(value = "0")
                ttk.Label(self.Acc, text = self.ACKeys[i]).grid(row = 4+2*LengthD, column = 1,sticky = 'w',columnspan = 1)
                ttk.Entry(self.Acc,textvariable=self.AccVars[i]).grid(row = 5+2*LengthD, column = 1,columnspan = 1)
                LengthD += 2
                
    def RecordAccounts(self):
        InputDate = self.date.get()
        for i in range(len(self.ACKeys)):
            Account = self.ACKeys[i]
            Value = self.AccVars[i].get()
            self.RecCom(Account,InputDate,Value)
        
class IncExpGrid:
    def __init__(self,master,Type,IncExps,NewCat,DeleteCat,RecordVal,prevdate,newrow):
        self.Cats = list(IncExps.keys())
        self.IEGrid = ttk.Frame(master)
        self.newrow = newrow
        self.Type = Type
        self.IncExps = IncExps
        self.RecIncExp = RecordVal
        

        self.prevdate = prevdate

        #Find Most recent date
        tempdates = []
  
        Dates = []
        Cats = []

        
        self.date = tk.StringVar(value = self.prevdate)

        for names in self.Cats:
            if IncExps[names].type == Type:
                Cats.append(names)
                TempDs = list(IncExps[names].values.keys()) #Could append directly to library
                for i in range(len(TempDs)): #And Remove duplicates somehow easily
                    if TempDs[i] not in Dates:
                        Dates.append(TempDs[i]) #List of all catagories and dates

        Dates.sort(reverse=True)
        self.Dates = Dates
        self.Cats = Cats

        ttk.Label(self.IEGrid, text = Type).grid(row = 0, column = 0, sticky = 'w')
        ttk.Button(self.IEGrid, text = "New Entry Date",command = self.New_Date).grid(row = 1, column = 0)
        ttk.Entry(self.IEGrid,textvariable = self.date).grid(row =1 , column = 1)
        ttk.Button(self.IEGrid, text = "Record Values: ",command = self.Record_Incexp).grid(row = 1, column = 4)
        ttk.Button(self.IEGrid, text = "New Catagory",command = lambda: NewCat(self.Type)).grid(row = 1, column = 2)
        ttk.Button(self.IEGrid, text = "Delete Catagory",command = DeleteCat).grid(row = 1, column = 3)

        #Start of main grid of expenses
        h=tk.Scrollbar(self.IEGrid, orient='horizontal')

        RS = 2

        #GridVal[Column][Row]
        self.GridVal = [[tk.StringVar(value = "0") for j in range(len(Dates))] for i in range(len(Cats)+2)]
        Grid = [[ttk.Entry(self.IEGrid,textvariable = self.GridVal[i][j]) for j in range(len(Dates))] for i in range(len(Cats)+2)]

        height = len(Dates)+1
        width = len(Cats)+2


        for j in range(height): #Rows
            Sum = 0
            for i in range(width): #Columns
                if j == 0:
                    if i ==0:
                        ttk.Label(self.IEGrid,text = "Dates").grid(row = RS+j, column = 0)
                    if i == width-1:
                        ttk.Label(self.IEGrid,text = "Total").grid(row = RS+j, column = len(Cats)+1)
                    if len(Cats)!=0 and i != width-1 and i != 0:
                        ttk.Label(self.IEGrid,text = Cats[i-1]).grid(row = RS+j, column = i)
                if j != 0:
                    k = j-1
                    if i == 0:
                        self.GridVal[i][k] = tk.StringVar(value = self.Dates[k])
                        Grid[i][k] = ttk.Entry(self.IEGrid,textvariable =self.GridVal[i][k]).grid(row = RS+j,column = i)
                    if i == width-1:
                        #Sum = sum([float(self.GridVal[i][k].get()) for i in range(1,len(self.GridVal[:][k])-1)])
                        self.GridVal[i][k] = tk.StringVar(value = Sum)
                        Grid[i][k]= ttk.Entry(self.IEGrid,textvariable = self.GridVal[i][k]).grid(row = RS+j,column = i)
                    if len(Cats)!=0 and i != width-1 and i != 0:
                        try: Val = self.IncExps[Cats[i-1]].values[self.Dates[k]]
                        except KeyError: Val = 0
                        self.GridVal[i][k] = tk.StringVar(value = Val)
                        Sum += float(Val)
                        Grid[i][k] = ttk.Entry(self.IEGrid,textvariable = self.GridVal[i][k] ).grid(row = RS+j,column = i)


        #h.config(command=text.xview)     
        #h.pack(side='bottom', fill='x')
    def New_Date(self):
        self.newrow(self.Type,self.date.get())

    def Record_Incexp(self):
        height = len(self.Dates)
        width = len(self.Cats)+1

        date = ''
        cat = ''

        for j in range(height): #Rows
            for i in range(width): #Columns
                if i == 0:
                    date = self.GridVal[i][j].get()
                if len(self.Cats)!=0 and i != 0:
                    cat = self.Cats[i-1]
                    value = self.GridVal[i][j].get()
                    self.RecIncExp(cat,date,value)

class CircleGraph:
    def __init__(self,master,Type,Profile,update):
        self.master = master
        self.Profile = Profile
        self.Type = Type
        self.Update = updateˆ
        self.F = ttk.Frame(self.master)

        if Type == "Overview":

            CBox = ttk.Combobox(self.F,textvariable = self.Date,validatecommand=self.Update,validate='focusout')
            CBox['values'] = self.DateList
            CBox.current()        


            fig = Fig(figsize = (5, 5),dpi = 100)
            # adding the subplot
            plot1 = fig.add_subplot(111)
            plot1.plot(y)
            # creating the Tkinter canvas
            # containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(fig,master = self.F)  
            canvas.draw()
            canvas.get_tk_widget().pack() # placing the canvas on the Tkinter window
            toolbar = NavigationToolbar2Tk(canvas,self.F)# creating the Matplotlib toolbar
            toolbar.update()
            canvas.get_tk_widget().pack()# placing the toolbar on the Tkinter window

        if Type == "Expenses":

        if Type == "Incomes":

        if Type == "Savings":

        if Type == "Grouping":

        if Type == "Vacation":

        if Type == "Graphs":





class Utilization:
    def __init__(self,master,IncExp,update,predate):
        self.master = master
        self.IncExp = IncExp
        self.F = ttk.Frame(self.master)
        self.Date = tk.StringVar()
        self.DateList = []
        self.Income = 0
        self.Expenses = 0
        self.Savings = 0
        self.Update = update
        self.Predate = predate

        Income = 0
        Expenses = 0
        Savings = 0

        ttk.Label(self.F,text = "Utilization").grid(row = 0, column = 0)
        ttk.Label(self.F,text = "Date").grid(row = 1, column = 0)
        ttk.Label(self.F,text = "Income: ").grid(row = 2, column = 0)
        ttk.Label(self.F,text = "Savings: ").grid(row = 3, column = 0)
        ttk.Label(self.F,text = "Expenses: ").grid(row = 4, column = 0)
        ttk.Label(self.F,text = "Remaining Budget: ").grid(row = 5, column = 0)

        Keys = list(IncExp.keys()) #Get Unique Dates and sort them with most recent first
        for i in Keys:
            for j in IncExp[i].dates:
                if j not in self.DateList:
                    self.DateList.append(j)
        self.DateList.sort(reverse=True)

        if self.DateList and predate == dt.date.today():
            self.Date = tk.StringVar(value = max(self.DateList))
        elif not self.DateList:
            self.Date = tk.StringVar(value = self.Predate)
        elif self.DateList and predate != dt.date.today():
            self.Date = tk.StringVar(value = self.Predate)
            
        CBox = ttk.Combobox(self.F,textvariable = self.Date,validatecommand=self.Update,validate='focusout')
        CBox['values'] = self.DateList
        CBox.current()

        
        for i in Keys:
            if IncExp[i].type == "Income":
                try: Income += float(IncExp[i].values[self.Date.get()])
                except KeyError: Income += 0
            if IncExp[i].type == "Expense":
                try: Expenses += float(IncExp[i].values[self.Date.get()])
                except KeyError: Expenses += 0
            if IncExp[i].type == "Savings":
                try: Savings += float(IncExp[i].values[self.Date.get()])
                except KeyError: Savings += 0


        Total = Income - Expenses - Savings
        self.Income = tk.StringVar(value = "$"+str(Income))
        self.Expenses = tk.StringVar(value = "$"+str(Expenses))
        self.Savings = tk.StringVar(value = "$"+str(Savings))
        self.Total = tk.StringVar(value = "$"+str(Total))
        
        CBox.grid(row = 1, column = 1)
        ttk.Entry(self.F,textvariable = self.Income).grid(row = 2, column = 1)
        ttk.Entry(self.F,textvariable = self.Expenses).grid(row = 3, column = 1)
        ttk.Entry(self.F,textvariable = self.Savings).grid(row = 4, column = 1)
        ttk.Entry(self.F,textvariable = self.Total).grid(row = 5, column = 1)

        
        


'''
class Groupings:

class Recurring:'''

        
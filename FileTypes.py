import datetime as dt


class Profile:
    def __init__(self,name,password,directory):
        self.name = name
        self.password = password
        self.directory = directory
        self.accounts = {}
        self.incexpcat = {}
        self.accdates = []
        self.catdates = []
        self.records = ''

    def New_Account(self,name,Type,color):
        self.accounts[name] = Account(name,Type,color,self.Acc_Date_Add)

    def Delete_Account(self,name):
        del self.accounts[name]

    def Acc_Date_Add(self,date):
        self.accdates.append(date)

    def New_IncExp_Catagory(self,name,Type,Color):
        self.incexpcat[name] = IncExpCatagory(name,Type,Color)   

    def Del_IncExp_Catagory(self,name):
        del self.incexpcat[name]

        

    def Save_Profile(self,directory):
        directory = directory + "/Profile" + self.name + ".txt"
        f = open(directory,'w')
        f.write(self.name)
        f.write(self.password)
        f.write("ACCOUNTS")
        AKeys = list(self.accounts.keys())
        IECKeys = list(self.incexpcat.keys())
        for i in AKeys:
            f.write(i)
        for i in IECKeys:
            f.write(i)
        f.close()

    def Load_Profile(self):
        print("HI")
        

class Account:
    def __init__(self,name,Type,Color,adddate):
        self.name = name
        self.values = {}
        self.type = Type
        self.color = Color

    def New_Value(self,date,value):
        self.values[date] = value
        adddate(date)

    def Delete_Value(self,date):
        del self.values[date]

    
class IncExpCatagory:
    def __init__(self,name,Type,color):
        self.name = name
        self.values = {}
        self.color = color
        self.type = Type

    def New_Value(self,date,value):
        self.values[date] = value

    def Delete_Value(self,date):
        del self.values[date]
        
        
class RecurringTransaction:

    def __init__(self,name,value,Type):
        self.name = name
        self.value = value
        self.type = Type

    def Change_Value(self,value):
        self.value = value







        

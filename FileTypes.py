import datetime as dt


class Profile:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.accounts = {}
        self.incexpcat = {}

    def New_Account(self,name,Type):
        self.accounts[name] = Account(name,Type)

    def Delete_Account(self,name):
        del self.accounts[name]

    def New_IncExp_Catagory(self,name,Type,Color):
        self.incexpcat[name] = IncExpCatagory(name,Type,Color)   

    def Del_IncExp_Catagory(self,name):
        del self.incexpcat[name]

    def Save_Profile(self,directory):
        print("Saved!")


class Account:
    def __init__(self,name,Type):
        self.name = name
        self.values = {}
        self.type = Type

    def New_Value(self,date,value):
        self.values[date] = value

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







        

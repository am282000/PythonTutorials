#Inheritance

'''
class Employee:
    increment =1.5
    
    def __init__(self,fname,lname,salary):      # parameterized contructor
        self.fname=fname
        self.lname=lname
        self.salary=salary
       
       
    def increase(self):    #self is necessary 
        self.salary= int(self.salary * self.increment)  # this will find it locally first than look in class 
       
    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split("-")
        return cls(fname,lname,salary)

    @staticmethod       # when we dont want to access local or global variables
                        #why static func ? so that we can put only our arguments .. no faltu arguments
    
    def isopen(day):
        if(day=="sunday"):
            return False
        else:
            return True
            

class Programmer(Employee):     #Inheritance
    def __init__(self,fname,lname,salary,lang,exp):
        super().__init__(fname,lname,salary)          #Programmer ki parent class ko call krna i.e. Employee
        self.lang=lang
        self.exp=exp
    
    #We can also redefine functions
    
    def increase(self):    #self is necessary 
        self.salary= int(self.salary * self.increment+5)  # this will find it locally first than look in class 
        # return self.salary     # If we write this That help will not return NOne 
    
        
harry= Programmer("harry","jackson",99000,"python",5)
print(harry.fname)
print(harry.exp)

print(help(Programmer))     #This will show all the structure of happening of code


print(harry.increase())
#Note: if we write print here ..it will give None .. i.e we are returning nothing !! Solution => Don't write print

'''



#Magic (means overloading) / Dunder method (inbuild methods) = 2 dunder methods are there repr, str 

'''
class Employee:
    increment =1.5
    
    def __init__(self,fname,lname,salary):      # Dundle init ..Argurment will automatically call when ever we  create an obj
        self.fname=fname
        self.lname=lname
        self.salary=salary
       
       
    def increase(self):    #self is necessary 
        self.salary= int(self.salary * self.increment)  # this will find it locally first than look in class 
       
    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split("-")
        return cls(fname,lname,salary)

    @staticmethod       # when we dont want to access local or global variables
                        #why static func ? so that we can put only our arguments .. no faltu arguments
    
    def isopen(day):
        if(day=="sunday"):
            return False
        else:
            return True
            

    #over loading   
    def __add__(self,other):
        return self.salary + other.salary
    
    def __repr__(self):     #It will take care of when we print .. what will display on screen
        return 'Employee({},{},{})'.format(self.fname, self.lname, self.salary)
    
    #overriding str dunder method 
    def __str__(self):
        return 'The name of Employee is {}'.format(self.fname,self.lname,self.salary)
        
harry= Employee("harry","jackson",99000)
rohan = Employee("rohan","jack",90)


# When we write + it will call inbuilt __add__ dunder method

a=6
# print(a.__add__(7))     #inbuilt dunder add 

# print(harry)    #normally this will give some hexadecimal value
print(repr(harry))
print(str(harry))   #I want this will will return only name of employee
print(harry+rohan)        #  + operator is overloaded
print(harry)        # By default also str vala call hoga

'''


# property 

class Employee:
    increment =1.5
    
    def __init__(self,fname,lname,salary):      # Dundle init ..Argurment will automatically call when ever we  create an obj
        self.fname=fname
        self.lname=lname
        self.salary=salary
        # self.email=fname+lname+"@gmail.com"  # if we declae it here after update it will not change
       
    def increase(self):    #self is necessary 
        self.salary= int(self.salary * self.increment)  # this will find it locally first than look in class 
       
    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split("-")
        return cls(fname,lname,salary)
    
    @property         # means take email as attribute instead of function
    def email(self):
        if self.fname == None:
            return 'Email not set'
        else:
            return self.fname+"."+self.lname+"@gmail.com"

    @email.setter
    def email(self,given_email):
        # self.email = given_email   #we cant do this directly
        name_list = given_email.split('@')[0].split('.')    #first split it with @ than with .
        self.fname = name_list[0]               #why .split('@')[0]  becoz we are taking rohan.khana nd spliting it again
        self.lname = name_list[1]
        
    @email.deleter
    def email(self):
        self.fname =None
        self.lname =None        #instead of deleating we are making thm as null

    @staticmethod       # when we dont want to access local or global variables
                        #why static func ? so that we can put only our arguments .. no faltu arguments
    
    def isopen(day):
        if(day=="sunday"):
            return False
        else:
            return True
            

if __name__=='__main__':
    harry = Employee('harry','jackson',99000)
    rohan = Employee('rohan','agarwal',9)
    
    print(harry.email,rohan.email)
    
    rohan.lname ='khana'
    print(rohan.email)      #we have to put email() if we dont used @property
    
    rohan.email='khana.rohan@gmail.com'   # we cant update it => to do this use setter
    print(rohan.email)
    
    
    del rohan.email         #Calling Deleter
    print(rohan.email)  
    
    
    
    
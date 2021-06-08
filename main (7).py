# Why OOPs => Code reusability

# Classes
'''
class Employee:
    pass        # This means i will make this class later ..dont give error

panda = Employee()      # objects
maddy = Employee()

# Do we really need to that name for every employee - Noooooo !!!
panda.fname ="Robot's"
panda.lname ="Panda"
panda.salary =44000

maddy.fname = "Madaan"
maddy.lname = "Sahaab"
maddy.salary =30000


print(maddy.fname)
print(maddy,panda)  #both objects are stored in different address
'''


# Making a class 

'''
class Employee:
    def __init__(self,fname,lname,salary):      # parameterized contructor
        self.fname=fname
        self.lname=lname
        self.salary=salary

panda = Employee("Robot's","Panda",44000)      #assining values to parameterized contructor
maddy = Employee("Madaan","Sahaab",77777)


print(maddy.fname)
print(maddy,panda)  #both objects are stored in different address
'''

# Variables 

'''
class Employee:
    increment =1.5
    NumberOfEmployee =0
    def __init__(self,fname,lname,salary):      # parameterized contructor
        self.fname=fname
        self.lname=lname
        self.salary=salary
        # self.increment=1.4     # Note if we declare this than self.salary take this one only
        Employee.NumberOfEmployee +=1
    def increase(self):    #self is necessary 
        self.salary= int(self.salary * self.increment)  # this will find it locally first than look in class 
        # self.salary= int(self.salary * Employee.increment)    # Direct global vala hi dekhe ga

print(Employee.NumberOfEmployee)

panda = Employee("Robots","Panda",44000)      #assining values to parameterized contructor
maddy = Employee("Madaan","Sahaab",77777)

print(maddy.salary)
maddy.increase()
print(maddy.salary)

maddy.job ="SDE"          #This will create a new instance i.e. local variable  (MAddy k personal variables hai )

print(maddy.__dict__)       #This will print all the local variables/ instance of classs

print(Employee.__dict__)    #This will print all the gloabl variables of classs

print(Employee.NumberOfEmployee)


'''


# Class Methods

'''
class Employee:
    increment =1.5
    
    def __init__(self,fname,lname,salary):      # parameterized contructor
        self.fname=fname
        self.lname=lname
        self.salary=salary
        # self.increment=1.4     # Note if we declare this than self.salary take this one only
      
    def increase(self):    #self is necessary 
        self.salary= int(self.salary * self.increment)  # this will find it locally first than look in class 
        # self.salary= int(self.salary * Employee.increment)    # Direct global vala hi dekhe ga
    
    @classmethod        #decorator
    def change_increment(cls,amount):
        cls.increment=amount
    

panda = Employee("Robots","Panda",44000)      #assining values to parameterized contructor
maddy = Employee("Madaan","Sahaab",77777)

print(maddy.salary)
Employee.change_increment(2)        #why ? made this ... coz i don't to all the objects again ..now we can change 
maddy.increase()                    #only one arguement
print(maddy.salary)

'''


# classmethod as alterbative of constructor 
# use ? when we need not to disturb local variables
# We can directly give the values of global params 

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


panda = Employee("Robots","Panda",44000)      #assining values to parameterized contructor
maddy = Employee("Madaan","Sahaab",77777)
chuza = Employee.from_str("chuza-chuhaa-88888")


print(chuza.fname)
print(chuza.lname)
print(chuza.salary)

'''

# staticmethod
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
            

panda = Employee("Robots","Panda",44000)      #assining values to parameterized contructor
maddy = Employee("Madaan","Sahaab",77777)
chuza = Employee.from_str("chuza-chuhaa-88888")

b= Employee.isopen("sunday")
print(b)






































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

class Employee:
    increment =1.5
    def __init__(self,fname,lname,salary):      # parameterized contructor
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    def increment(self):
         


panda = Employee("Robot's","Panda",44000)      #assining values to parameterized contructor
maddy = Employee("Madaan","Sahaab",77777)

maddy.increment()
print(maddy.fname)
print(maddy,panda)  #both objects are stored in different address

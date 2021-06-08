# Loops
'''

# To print all the item in list

# li=[777,143,"Hii"]        #List
# li=(777,143,"Hii")        # Tuple
# li={777,143,"Hii"}          #Set

li={                        #Dictionary - Note this will only print Roll and Name
    "Roll":777,
    "Name":"Hii"
}
for item in li:
    print(item)
    
    
'''


#While Loops

'''
i=0;
while(i<10):
    print(i)        #This will print 0 to 9
    # print(i+1)      #This will print 1 to 10
    i=i+1;

'''

# Break 
'''
i=0;
while(i<10):
    i=i+1;
    if i==7:
        break       #Break the loop here
    print(i)        
'''
# Continue
'''
i=0;
while(i<10):
    i=i+1;
    if i==7:
        continue    # Forget 7 and keep moving
    print(i)        
'''

# Functions
'''
def greet():        # def funcName ():
    print("Good Morning")

greet()         #Calling of function


def sum(a=12,b):        # a having default arguement
    c=a+b
    return c

d=sum(34,54)    
print(d)

'''

# Python is an OOP language

class Employee:
    def __init__(self,name,salary):     # Contructor = def __int__(objectName):  NOte objName is mandatory than write params is needed 
        self.name = name
        self.salary = salary
        
emp =Employee("ashish",20000)
print(emp.name)
print(emp.salary)
































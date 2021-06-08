
'''
lst=[2,3,4,61,61,5,61]
print(lst)
var=type(lst)
print(var)
var=lst[1:3]
print(var)
var=lst[3]
print(var)
lst[3]=77
print(lst)
var=len(lst)
print(var)

lst.append(100)         #Add element at last
print(lst)

lst.insert(1,200)       #add 200 at 1st index  -> thn it shift all other elements accordingly

print(lst)

lst.remove(61)          #first occuring 61
print(lst)

lst.pop()
print(lst)

del lst[1]              #delthat index value
print(lst)

lst.clear()         #To clear the whole list
print(lst)

del lst             #to delete the whole list


'''

# Tuple

# We cant change tuple elements

'''
a=("Baby" , "Panda" , "Chuha")
print(a)
print(type(a))

# a[0]="Robo"         #We can't cahange tuple elements


a=list(a)   # this is how we can typecast a tuple to list
a[0]="Robo"         #Now we can change list elements
print(a)
print(type(a))

'''


#set

'''
s1={2,2,2,2,2,2,2,3,22,2,2,5,6,7,8,9}   # it will print the unique elements ... avoid duplicacy
print(s1)

# set, update, add

s1.add(444444)      # Add element at last
print(s1)

s1.update([1,3,4,5,66,3,3,3,3,21,12,1,9,999])
print(s1)

print(len(s1))
s1.remove(1)        # if give a no that is not in set than it will give error
print(s1)

s1.discard(166666)   # this one is better if hai than remove ni to ignore
print(s1)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z)

z = x.union(y) 
print(z)

print("Welcome to" , end = ' ') 
print("GeeksforGeeks", end = ' ')


# .pop,.clear,del,intersection ,union, end  = we can use all this


'''


# Dictionary

# Key value pair 

'''
madDict={
    "Name":"Maddy",
    "Class":"B.tech",
    "CGPA":8.4,
    "Stream": "cs"
}

print(madDict)
# print(madDict[0])       #Key error
print(madDict["Name"])

madDict["Name"]="Chuzaa"
print(madDict["Name"])
print(madDict)


# Functions almost same .... Google it 

madDict.pop("Name")
print(madDict)

'''

# Boolean datatype 

'''
a=True
b=False
'''

# Conditional statements

'''
age=input("Enter your age\n")   # input function take evrything as str value ..
                                # to convert it into another we have to type cast it
# print(age)
age=int(age)
# print(type(age))

if(age>19):
    print("You are bada bachaaa")
elif(age==19):
    print("You are meraa babyyyy")
else:
    print("You are chotuuu bachaaa")

'''

# Loops 

# How to print a no b/w 1 to 100

for i in range(0,100):
    # print(i)    # print from 0 to 99
    # print(i+1)  # print from 1 to 100


li=[143,]


1:29:00









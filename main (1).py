# string

name1 ="Hi"
name2="I am"
name3='''Madaan 
Sahaab'''
print(name1)
print(name2)
print(name3)
print(name1[0])
print(name3[2:4])     #means 2nd index to 3rd index   - string slicing

name4="     Madd yyy     "
print(name4)
print(name4.strip())   # strip all the extra white spaces
print(len(name1))       #length of string


name5 = "HeyaaBabbbyyyy"
var=name5.lower()
print(var)
var=name5.upper()
print(var)

var=name5.replace("a","i")    # Replace all a to i
print(var)

var=name5.replace("eyaa","i")    # Replace all eyaa to i
print(var)

name=" Panda , Chuhha , Chuzaa "    #Usefull in cases like
var =name.replace(",","\n")
print(var)


stri ="This is called as "
stri2 ="Concatination"
print(stri + stri2)         #Cooncatination of strings


p1="Madaan Sahaab"
p2="Programmer"
temp="This is {1} and I am a {0}".format(p1,p2)      # by default {0}   {1} hota h isme if wanna switch write {1}{0}
print(temp)



# fstream feature 

# name ="Madaan"
# age="20";
# temp = f"This is {name} and he is {age} y/o"
# print(temp)

'''
Python Collection :
1. List 
2. tuple
3. set
4. dictionary
'''
















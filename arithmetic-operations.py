# x = int(input( "Please enter valure for x="))
# y = int(input( "Please enter valure for y="))

# print (x+y)
# print (x-y)
# print (x/y)
# print (x*y)
# print (x%y)



# # Below type will tell which type of function you have used in variables 
# typex = type(x)
# typey = type(y)
# print(typey)

# z = 45
z = "45"
z = int(z)
print (z)
typez = type(z)
print (typez)

a = "45"
a = float(a)
print (a)
typea = type(a)
print (typea)



# String slicing

# name = 'Pratik'
# name1 = "Akshay"
# name2 = ''' Pratik 
# and Akshay both my names '''
# print (name[3:5])
# print (name1[2:5])
# print (name2[1:5])

#  print perticular number character in the variable 

# name = 'Pratik'
# name1 = "Akshay"
# name2 = ''' Pratik 
# and Akshay both my names '''
# print (name[3])
# print (name1[5])
# print (name2[10])

# Stripping
name = "        Pratik, Milind, Dhumane"
print (name)
print (name.strip())
print (len(name))      # this will give us length of variable 


var = name.lower()
var = name.upper()
var = name.replace("t","T")
var = name.replace (",","\n")
print(var)

name = "Pratik "
middlename = "Milind "
surname = "Dhumane"

print(name + middlename + surname)

# temp = "My name is {2} {0} {1}".format(name, middlename, surname)
temp = f"My name is {surname} {name} {middlename}"
print (temp)

# Python Collection
# 1. List
lst = [61,2,3,4,6,45]
# listing = type(lst)
lst[2] = 46
listing = lst[2]
# lst.append(1945)
# lst.insert(3,1945)
# lst.pop()
del lst[4]
listing = lst
# listing = lst [2:5]
print(listing)

#2. tuple
a = ("Pratik", "Akshay", "Dhumane")
var = a
# var = type(a)
a = list(a)
a[2] = "Milind"
print(var)
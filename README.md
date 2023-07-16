print is function
In "" string

Example:
print("Hello World\n")

Import - 
Use the import keyword to make code in one module available in another.
Module - 
A Python module is a file containing Python definitions and statements

Variables
Integer 	a = 40
String 		b = “pratik”
Floating	c = 20.36

Everything which is in double inverted comma that is string “”
Rules to create variable
Variable should not start with an integer
Variable should start with a letter or an underscore
It can only contain alphanumeric characters
Variable name are case sensitive ie. Pratik and pratik are two different variables

Arithmetic operations 
x = int(input( "Please enter valure for x="))
y = int(input( "Please enter valure for y="))


print (x+y)
print (x-y)
print (x/y)
print (x*y)
print (x%y)


# Below type will tell which type of function you have used in variables
typex = type(x)
typey = type(y)
print(typey)

TypeCasting
Here in below example
 z=36 	  is an integer but
 z=”36” is a string 
Now if you want to call string into an integer you have to write 
z=”36”
Z = int (z)
Z = 40
z = "36"
z = int(z)
print (z)
typez = type(z)
print (typez)
Similarly you can convert into float as well
Z = 36
z = "36"
z = float(z)
print (z)
typez = type(z)
print (typez)

String 
# String


name = 'Pratik'
name1 = "Akshay"
name2 = ''' Pratik
and Akshay both my names '''
print (name)
print (name1)
print (name2)

Output
[Running] python -u "/Users/pratik/Documents/scripting/python-scripting/arithmetic-operations.py"
Pratik
Akshay
Pratik
and Akshay both my names

print 0th character in your variable
Now, to print 0th character in your variable you can use print (name[0]) 
Where [0] will help you to get the 0th character in the name variable 
name2 = ''' Pratik
and Akshay both my names '''
print (name[0])

For example 
# String


name = 'Pratik'
name1 = "Akshay"
name2 = ''' Pratik
and Akshay both my names '''
print (name[0])
print (name1[1])
print (name2[2])
 And output is
P
k
r

String Slicing 
name = 'Pratik'
name1 = "Akshay"
name2 = ''' Pratik
and Akshay both my names '''
print (name[3:5])
print (name1[2:5])
print (name2[1:5])
Output
ti
sha
Prat

Here [3:5] used to slice the string 
3 is 3rd character in the variable [ it will start printing from 3rd character]
5 is actually 5-1 = 4th character in the variable [ it will print upto 4th character]

Stripping 
Removes extra spaces from before and after 
name = " Pratik "
print (name)
print (name.strip())
print (len(name)) # this will give us length of variable
Output
      Pratik       
Pratik
28


To print variable in upper and lower case
name = " Pratik "
print (name)
var = name.lower()
candy = name.upper()
print(var)
print(candy)
Output
        pratik              
        PRATIK   
To change/replace  any letter in variable 
name = " Pratik "
change = name.replace("t","T")
print(change)
Output 
PraTik


To connect or add two strings
name = "Pratik "
middlename = "Milind "
surname = "Dhumane"


print(name + middlename + surname)


temp = "My name is {}{}{}".format(name, middlename, surname)
print (temp)
Here in variable temp {} bracket can be filled later with variable using .format (name, name2) like this way 
Output 
Pratik Milind Dhumane
My name is Pratik Milind Dhumane
 
And to change the positions of variable use below
name = "Pratik "
middlename = "Milind "
surname = "Dhumane"


print(name + middlename + surname)


temp = "My name is {2} {0} {1}".format(name, middlename, surname)
print (temp)


#By default it is 
#temp = "My name is {0} {1} {2}".format(name, middlename, surname)
Output
My name is Dhumane Pratik  Milind 


To bypass above things f string introduced
name = "Pratik "
middlename = "Milind "
surname = "Dhumane"


print(name + middlename + surname)


# temp = "My name is {2} {0} {1}".format(name, middlename, surname)
temp = f"My name is {surname} {name} {middlename}"
print (temp)
Output will be the same 
My name is Dhumane Pratik  Milind 



Python Collection
List
Tuple
Set
Dictionary
# 1. List
lst = [61,2,3,4,6,36]
listing = type(lst)
listing = lst[2]
listing = lst [2:5]
print(listing)
Output 
<class 'list'>
3
[3, 4, 6]
We can change numbers as well in variable list
lst = [61,2,3,4,6,36]
lst[2] = 46
listing = lst[2]
listing = lst
Output 
[61, 2, 46, 4, 6, 36]

Lst.append will add element at the end of the list and print 
lst = [61,2,3,4,6,36]
# listing = type(lst)
lst[2] = 46
listing = lst[2]
lst.append(1936)
Listing = lst

Output 
[61, 2, 46, 4, 6, 36, 1936]

Lst.insert
lst.insert(3,1936) 
Here 3 represents the number of position to add element in the list 
And 1936 is the element to add
lst = [61,2,3,4,6,36]
# listing = type(lst)
lst[2] = 46
listing = lst[2]
lst.insert(3,1936)
Listing = lst

Output 
[61, 2, 46, 1936, 4, 6, 36]

To remove any last element from the list 
lst.pop

lst = [61,2,3,4,6,36]
# listing = type(lst)
lst[2] = 46
listing = lst[2]
lst.pop()
Listing = lst
Output
[61, 2, 46, 4, 6]

To delete any particular position element in the list 
del
lst = [61,2,3,4,6,36]
lst[2] = 46
listing = lst[2]
del lst[4] 
Listing = lst
Output 
[61, 2, 46, 4, 36]

2. Tuple [ you can not override the values in tuple]
#2. tuple
a = ("Pratik", "Akshay", "Dhumane")
var = a
var = type(a)
print(var)
Output
<class 'tuple'>

a = ("Pratik", "Akshay", "Dhumane")
var = a
a[2] = "Milind"
print(var)
Output 
    a[2] = "Milind"
TypeError: 'tuple' object does not support item assignment
But you can convert tuple to list and list to tuple
a = ("Pratik", "Akshay", "Dhumane")
var = a
a = list(a)
a[2] = "Milind"
print(var)
Output 
('Pratik', 'Akshay', 'Dhumane')

# -*- coding: utf-8 -*-
"""13-12-19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qehwXE3X3KB1-9MtTZ77OiH1F3W0GRQ1
"""



"""#markdown
##markdown
###markdown
# insert site [SITE](https://login.gitam.edu/Login.aspx)
# insert image 
![site](https://image.shutterstock.com/image-photo/bright-spring-view-cameo-island-600w-1048185397.jpg)
# Python basics
### Python is easy to learn.
###pyhton is a begineers language

# creating order list
1.abs
2.hsdf
    1.a
    2.b
[]
# unordered list
1.abs
2.hshsh
3.ggtdgdgdd

# bold and italic
**BOLD**

*ITALIC*
"""

print("HELLO WORLD")

#Variable creation
x=10
y=20
x+y

"""# Rules for variable
- name should begin with a character
- no special characters allowed except underscore (_)
"""

name = "junaid"
age = 20
print("my name is:",name ,"my age is ",age)

name = input ("**Enter  name**")
age= int(input ("enter age"))
print("Your name is:",name, "Your age is:",age)

X= int(input("enter the value of X : "))
Y= int(input ("enter the value of Y : "))
print("addition of X and Y :",X+Y)

print(" multiplication of X and Y :",X*Y)

print("subtraction of X and Y :",X-Y)

print("division of X and Y :",X/Y)

"""#Funadamental dataypes 

* int 
* float
* complex
* boolean
* string
"""

x = 12
y=20.2
z= 5+6j
print(type(x))
print(type(y))
print(type(z))

c=complex(2,5)
print(c)

c1=5+4j
c2=6+7j
print("addition of complex values", c1+c2)
print("subtraction of complex values", c1-c2)
print("a=multiplication of complex values", c1*c2)
print("division of complex values", c1/c2)

#boolean
x=6
y=7
x < y

#string 
s1="abd"
s2="dfg"
print(type(s1))
print(type(s2))

i=100
print(type(i))
s1=str(i)
print(type(s1))
f1=float(i)
print(type(f1))

#lenght
a= "abcd"
print(len(str(a)))

n1= 100 #single variable
a=b=c=20 #multiple variable assignment
a1,b1,c1 = 123,234,345
print(n1)
print(a,b,c)
print(a1,b1,c1)

"""# precendence of Arth operators
* paranthesis
* power
* Multiplication
* Addition
"""

x= 1+2 ** 3/4*5
print(x)

"""#operators
* arithmetic operators
- -
- *
- /
- %
- **
- //  
- +

# Relational operators
* == , !=,<,>,<=,>=

#logical operators
* and
* or 
* not
"""

i=100
a1=(i>15) and (i>76)
a2=(i>567) or (i>3456)
print(a1)
print(a2)
print(not i)

"""#Membership operator
 * in
 * not in
"""

str1= "abc"
print('a' in str1)
print('a' not in str1)

"""#control flow statement
* conditional statement
* looping statement
* if-else statement
* syntax

    if condition :
                  statements
    else         
         statements
"""

#check the given number is even or odd
n= int(input("enter a number"))
if n%2 == 0:
     print("even")
else:
    print("odd")

#check the given number is perfectly multiple of 3 and 5
n= int(input("enter a number : "))
if n%3== 0 and n%5==0:
                    print("YES")
else:
    print("NO")

#check the given number is positive , negative or zero
A=int(input("enter the number"))
if A>0: 
      print("the given number is positive")
elif A<0 :
     print("the given number is negative")
else :
     print("the given number is zero")

#LEAP YEAR
n=int(input("enter year"))
if n%400==0:
  print("Its a leap year")
elif n%4==0 and n%100!=0:
    print("its a leap year")
else:
      print("its not")
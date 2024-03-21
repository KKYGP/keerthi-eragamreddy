#variables
#a=7,8
#print(a)
#print(type(a))
#---->swaping of variables
'''a=5
b=2
temp=a
a=b
b=temp
print(a,b)-only in python
a=3
b=2
c=0
a,b=b,c=c,a
print(a,b,c)
'''
a=2.3
b=42
#a=a+b
#b=a-b
#a=a-b
a=a*b
b=a/b
a=a/b
print(a,b)
#id()-->it is used to find the memory address of the variable
#--->KEY WORDS
'''**KEYWORDS ARE RESERVED WORDS WHICH PROVIDES SPECIAL MEAANING TO COMPILER OR INTERPRETER'''
import keyword
print(len(keyword.kwlist))
#to check if string is keyword or not
print(keyword.iskeyword("as"))
#--->LITERALS
#->Literal is the constant value assigned to a variable
#->a variable is considers to be constant when it is defines
#hash()-->it creates a hash value for constant datatypes
p1= (743,2,3)
print(hash(p1))
n1=23+2j
print(hash(n1))
#n1=[2,3,4]
#print(hash(n1))
a=7
b=7
print(id(a))
print(id(b))
#OPERATORS
'''->Arithmctic
->assignment
->logical
->relational or comparison
->bitwise
->identify
->membership'''
'''a=8
b=6
c=9
print(a+b+c)
#-->FLORE DIVISION OPERATOR
a=3456
b=678
print(a//b)#floor division
a=34
print(a**2)#power of a number
#ASSIGNMENTS
a=8
a+=2
print(a)
a=10
a-=10
print(a)
a=10
a&=2
print(a)
#COMPARISON
a=3
b=2
print(a>b)'''
'''n1=int(input("enter the value"))
if n1%2==0:
    print(n1,"even")
else:
        print(n1,"odd")'''
name=input("enter your name")
age=int(input("enter your age"))
nationality=input("enter your nationality")
if age>18 and nationality=="indian":
    print("eligible")
else:
    print("not eligible")





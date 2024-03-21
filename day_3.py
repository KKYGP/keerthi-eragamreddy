'''
--->n= input("enter the length value")
n1= input("enter the breadth value")
if n == n1:
    print("square")
else:
    print("not square")
n=input("enter your age")
n1=input("enter your age")
n2=input("enter your age")

---->n=int(input("enter your number"))
if n%5==0 and n%7==0:
    print("multiple")
else:
    print("not multiple")
---> car price 
price=int(input("enter bike price"))
if price>100000:
        discount = price*(6/100)
        value = price-discount
        tax=value*(15/100)
        total=value+tax
else:
    tax =price*(5/100)
    total=price+tax
print("total amount",total)
    
--->we can't able to give condition for else
--->more than one condition we use elif condition

--->find greater in 3
a=2
b=6
c=2
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
        print("b is greater")
else:
    print("c is greater")
--> grades of school marks
marks = int(input("enter your marks"))
if marks<=25:
            print("F")
elif marks>=25 and marks<45:
            print("E")
elif marks>=45 and marks<50:
            print("D")
elif marks>=50 and marks<60:
            print("C")
elif marks>=60 and marks<80:
            print("B")
elif marks>=80:
            print("A")
--->SHORT HAND
**RULES
->statement inside condition have to be execute first
->elif cannot be used in short hand if else
->always it have to endeith else


char =input("enter alphabet")
if char  == 'a' or char == 'e'or char == 'i' or char == 'o' or char == 'u':
    print("vowel")
else:
    print("consonant")
char =input("enter alphabet")
str1 = "aeiouAEIOU"
if char in str1:
    print("VOWEl")
else:
    print("consonant")
---->shorthand if else
---> vowel or not
char =input("enter the char")
str1="aeiouAEIOU"
print("VOWELS") if char in str1 else print("consonent")
--->greter of 3
a=3
b=4
c=1
print("a is greater") if a>b and a>c else print("b is greater") if  b>a and b>c else print("c is greater")
--->LOOPING CONCEPTS
**looping an be implimented using
->for loop
for loop is used for iteartion ,if we know the number of times the loop have to run
it is used to iterate eg(string,list,tuple,etc..)
-->for syntax :
for userdefined_variables in range(start,end,step)
statement
statement
statement
Eg:to print the values from 1 to 10
for i in range(0,11):
    print(i)
Eg:2
for i in range(12, 50,2):
    print(i)
for i in range(1,20):
   print("keerthi")
Eg:3
to decrement the value
for val in range(20,1,-2):
    print(val)
Eg:4
for val in range(1,10+1):
     print('7','X', val,'=' ,val*7)
----> FORMAT FUNCTION
for val in range(1,10+1):
ans="7 x {} = {}"
 print(ans.format(val,val*7))
    print(f"7x{val}={val*7}")
--->BREAK
IT IS USED TO TERMINATE THE LOOP
for i in range(1,10):
    if i==6:
        break
    print(i)
for i in range(1,10):
    if i==6:
      print(i)
      break
for i in range(1,10):
    print(i)
    if i==6:
      break
----->>CONTINUE STATEMENT
Eg:1
for i in range(1,10):
  if i==5:
    continue
  print(i)
--->PRACTICE PROBLEMS
1.EVEN NUMBERS BETWEEN 20 AND 40
for i in range(20,40):
 if i%2==0:for odd i%2!=0
    print(i)
---->WHILE LOOP
**IT IS USED WHEN WE DONT KNOW THENUMBER OF TIMESTHE LOOP HAVE TO RUN
**TO ITERATE THE NON INTERABLE ELEMENTS WHILE LOOP IS USED
SYNTAX:
    INTILIZATION
    WHILE CONDITION:
        STATEMENT
        INCRE OR DECRE
-->TO DISPLAY SUM OF ODD AND EVEN NUMBERS NUMBERS THAT FALL BETWEEN 12 AND 37 
i = 0
while i<11:
    print(i)
    i =i+1
i=10
while i>0:
      print(i)
      i-=1'''

        





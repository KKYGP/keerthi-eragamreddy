'''
--->BREAK USING WHILE LOOP

num=20
while num<=30:
    if num==27:
        break
    print(num)
    num+=1
--->num=20
while num<=30:
        print(num)
        num+=1
        if num==27:
           break

--->num=20
while num<=30:
        print(num)
        if num==27:
           break
        num+=1
--->num=20
while num<=30:
 if num==27:
        print(num)
        break
 num+=1

----->CONTINUE STATEMENT

-->num=20
while num<=30:
 if num==27:
     continue
 print(num)
 num=num+1
--->num=20
while num<=30:
    num= num+1
    if num==27:
     continue
    print(num)
--->i=12
sum =0
while i<23:
    sum=sum+i
    i+=1
print(sum)

--->AVG
i=20
sum=0
while i<26:
  sum=sum+i
  avg=(sum)/6
  i+=1
print(avg)--->22.5
--->i=20
sum=0
count=0
while i<=30:
  sum=sum+i
  count+=1
  i+=1
print(sum/count)--->25.0

!---->NESTED FOR LOOP
-->for i in range(1,3+1):
 for j in range(1,5):
   print(i,j)

--->for row in range(1,5):
    for col in range(1,5):
        print("*",end=" ")
---->for row in range(4):
    for col in range(4):
        print("*",end=" ")
    print()    -->output
                  * * * *
                  * * * *
                  * * * *
                  * * * *

-->rows= int(input("enter the row"))
cols= int(input("enter the col"))

for row in range(rows):
    for col in range(cols):
        print("*",end=" ")
    print()
--->rows= int(input("enter the row"))
cols= int(input("enter the col"))

for row in range(rows):
    for col in range(cols):
        print(row,end=" ")
    print()
rows= int(input("enter the row"))
cols= int(input("enter the col"))
--->sum=0
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum,end=" ")
    print()

--->for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print()

for row in range(0,6):
    for col in range(0,6-row):
        print("*",end=" ")
    print()
    
for row in range(6):
    for col in range(6):
        if col==0 or col==5 or row == 0 or row == 5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for row in range(0,6):
    for col in range(0,8):
        if ((row==0 and col==3)or (row==1 and (col>=2 and col<=4) or (row==2 and (col>=1 and col<=5 )))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
---->DATA TYPES
->PRIMARY
->COLLECTION
PRIMARY:
    ->NUMBER
    ->STRING
    ->BOOLEAN
    ->NONE
COLLECTION:
    ->LIST
    ->TUPLE
    ->SET
    ->DICTONARY
LIST:IF THE COLLECTION OF ELEMENTS ARE SURRONDED BY SQUARE BRAKETS,IT IS CONSIDERED AS LIST
CHARACTERISTICS:
    ->LIST HAVE SURROUND BY []
    ->IT IS MUTABLE(THE ELEMENTS IN THE LIST ARE CHANGABLE)
    ->EVERY ELEMENT INSIDE LIST IS INDEXED
    ->THE ELEMENTS INSIDE THE LIST WILL BE ORDERED FORMAT
    ->IT CAN HOLD DUPLICATE VALUES
    ->ITS HETEROGEROUS
TO ACCESS THE ELEMENTS IN LIST
l1 = [1,4,1,7,82.9,"K","I"]
print(l1)
-->INDEXING:
    IN THE COLLECTION DATATYPES LIKES LIST,TUPLE,STRING,THE ELEMENTS WILL BE ALLOTED WITH PRE-DETERMINED UNIQUE VALUE CALLED INDEX VALUE
-->WE HAVE 2 TYPES OF INDEXING
**POSITIVE INDEXING--STARTS WITH 0 FROM LEFT HAND SIDE
**NEGATIVE INDEXIND--STARTS WITH -1 FROM RIGHT HAND SIDE
-->POSITIVE INDEXING
lst1=[1,"g",3,4,"kr"]
print(lst1[1])
print(lst1[4])
---->NEGATIVE INDEXING
lst2=[2,3,4,5,6,]
print(lst2[-3])
---->SLICING:
lst=[1,3,4,"k","y"]
print(lst[0:4])
lst=[1,3,4,"k","y"]
print(lst[3:5])
print(lst[:6])
print(lst[-3:-1])
print(lst[:])
print(lst[0:5:2])
print(lst[-1:-4])
print(lst[-4:-1])
print(lst[-5:-1:2])
lst=[1,4,1,7,8.29,"k","l","o"]
print(lst[-7:-1:2])
-->APPEND
l1=[7,8,9,0]
l1.append("keerthi")
print(l1)
--->when we use append whatever we give for list it is added in last of the list'''




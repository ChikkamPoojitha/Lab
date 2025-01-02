ch=input("enter your name: ")
print(ch[::-1])
for n in ch:
   if (n=="a" or n=="e" or n=="i" or n=="o" or n=="u"):
     print(n)
#transfer statements-break(comes out of the loop),continue(skip the current iteration),pass(goes to the next statement)
#string functions
"""find,'''split''',replace,count,upper,lower,swapcase,title,format""" 
#aliasing- the process of giving another reference variable to the original variable.their names are differenet but memory add is same
"""ex l1=[1,2.3,4,5]
      l2=l1
      print(id(l1))
      print(id(l2))"""

#copy()-cloning
#program to add items into a tuple
#packing and unpacking
a=10
b=20
c=30
d=40
t1=a,b,c,d #packing
print(t1)
a,b,c,d=t1 #unpacking
print("a=",a,"b=",b,"c=",c,"d=",d)
#variable length argument-we can pass as many as arguments we want
#syntax- def f1(*n)
def summation(*n):
   total=0
   for i in n:
      total=total+i
   print("the sum is: ",total)
summation()
summation(10)
summation(10,20)
summation(10,20,30)
l1=[]
for i in range(1,6):
        sq=i*i
        l1.append(sq)
print(l1)   

def sq(n):
    return n*n
l1=[1,2,3,4,5]
sqaures=map(sq,l1)
print(list(sqaures))

#decorator()-a function which takes a function to modify the existing functinality of a function -------> check code online
'''def decor(func):
    def inner(name):
        if name=="steve":
            print("hello",name,"bad morning")
        else:
            func(name)
        return inner 
@decor
def wish(name):
        print("hello",name,"good morning")
wish("john")
wish("steve")'''  

##EXCEPTION HANDLING

#Generator function: this function produces a sequence of numbers
#def functionName():
   #yeild "l1"
   #yeild "l2"
def countdown(num):
    print("start countdown")
    while(num>0):
        yield num 
        num=num-1
values=countdown(10)
print(values)
for i in values:
    print(i) 
#write a python program to develop a simple calculator which performs the four basic operations +-/*
n1=int(input("enter the n1"))
n2=int(input("enter n2"))
o=input("enter the operator")
def add(n1,n2):
    print(sum)
def sub(n1,n2):
    #sub=n1-n2
    return sub
def mul(n1,n2):
    #mul=n1*n2
    return mul
#def div(n1,n2):
   # div=n1/n2
    #return div
if (o=="+"):
    sum=n1+n2
elif(o=="-"):
    sub=n1-n2
else:
    mul=n1*n2        
 
add(5,10)
print(sub(5,10))
mul(5,10)
#div(5,10)



#interger

#syntax:

'''variable_name = value'''

#Float

'''variable_name = value'''

#Examples:

a=10
print(a)

a=10
b=20
c=a+b
print(a+b)

a1=input('enter first number:')
b2=input('enter second number:')
sum=float(a1)+float(b2)
print('the sum of{0} and{1} is{2}'.format(a1,b2,sum))

a=b=c=5
print(a,b,c)

a,b,c,d=10,20.5,"python",'true'
print(a,b,c,d)
print(d,c,b,a)

#format()function
txt="my name is {fname},i'm {age}years old.".format(fname="yashu",age=23)
print(txt)

txt="my name is{0},i'm {1}year old.".format("nandu",18)
print(txt)

#Data types:
#string
x="thundersoft"
print(x) #display x
print(type(x))#display the data type of x:

#integer
x=20
print(x)#display x
print(type(x))#display the data type of x:

#float
x=20.5
print(x)#display x:
print(type(x))#display the data type of x:

#complex
x=1j
print(x)#display x:
print(type(x))#display the data type of x:

#list:
x=["yashu","nandu","kavya"]
print(x)#display x:
print(type(x))#display the data type of x:

#implicity
a=7
print(type(a))
b=3.0
print(type(b))
c=a+b
print(c)
print(type(c))
d=a*b
print(d)
print(type(d))

#explicit
#int to float
a=5
n=float(a)
print(n)
print(type(n))

#float to int
a=5.9
n=int(a)
print(n)
print(type(n))

#MATH OPERATIONS
#ceil()
import math
x=33.7
y=-13.1
print("The ceil of 33.7 is :",math.ceil(33.7))
print("The ceil of 13.1 is :",math.ceil(13.1))

#floor
import math
print("The floor of 33.7 is:",math.floor(33.7))
print("The floor of 13.1 is :",math.floor(13.1))

#sqrt()
import math
print(math.sqrt(0))
print(math.sqrt(4))
print(math.sqrt(3.5))

#abs()
abs(-7)
print(abs)

#id()function
x="python"
y=id(x)
print(y)

x=('yashu','nandu','kavya')
y=id(x)
print(y)

x=id("python")
y=id(x)
print(y)

#function declaration

def sum():
    print("In sum function")
sum()

def diff():
    print("in diff function")
diff()

#local and global variables
def m1(): #local variable
    a=10
    print(a)
    return
def m2():
    a=20
    print(a)
    return
m1()
m2()

a=30
def m1(): #global variable
    print(a)
    return
def m2(): #local variable
    a=20
    print(a)
    return
m1()
m2()
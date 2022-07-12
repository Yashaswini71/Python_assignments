#Basic Syntax

'''def fun_name ():
    statement1
    statement2'''


    #Types of functions:

# 1. Function without arguments and without return type

def fun_name():
    print("hello world")

fun_name()

#  2. Function without arguments and with return type
     
def fun_name():
    return "hello world"
str=fun_name()

#   3. Function with arguments and without return type

def fun_name(a,b):
    print ("sum=",a+b)
fun_name()

#4. Function with arguments and with return type

def fun_name(a,b):
    return a+b
sum=fun_name()

#5. Function with variable num of arguments

def fun_name(*tuple):
    result=1
    for i in tuple :
        result=result*i
    print(result)
fun_name(2,3,4,5)

#6. Default Arguments

def fun_name(num1=5,num2=4):
    result=num1+num2
    print("result=",result)
fun_name()

#7. keyword Arguments

def fun_name(num1=5,num2=4):
    result=num1+num2
    print("result=",result)
fun_name(num2=9,num1=6)






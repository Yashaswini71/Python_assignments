#operators

'''
Types of Operator

1)Arithmetic Operators
+ - * / % ** //

2)Comparison (Relational) Operators
> < >= <= == !=

3)Assignment Operators
= += -= /= **= *= %=

4)Logical Operators
and or not

5)Bitwise Operators
& | ^ >> << ~

6)Membership Operators
in  not in

7)Identity Operators
is  is not
'''


#Arithmetic Operators

#operators
#arthmetic operators
x = 5
y = 3
print(x + y)#addition

#subtraction
x = 5
y = 3
print(x - y)

#multiplication
x = 5
y = 3
print(x * y)

#division
x = 12
y = 3
print(x / y)

#modulus
x = 5
y = 2
print(x % y)

#Exponentiation
x = 2
y = 5
print(x ** y)

#floor division
x = 15
y = 2
print(x // y)

#assignment operators
x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

#Comparison operators

x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x <= y)


#bitwises operators

a = 8
b = 2
c = a ^ b 
print(c)

print("Bitwise &")
a = 0xf0
b = 0x0f
c = a & b
print(c)

print("Bitwise |")
a = 0xf0
b = 0x0f
c = a | b
print(c)

print("Bitwise <<")
a = 8 
b = a << 1  #a * 2**shift
print(b)

print("Bitwise >>")
a = 8
b = a>>1 # a / 2**shift
print(b)

print("Bitwise ~")
a = 0
b = ~a



#logical operators
x = 5
print(x > 3 and x < 10)#and

x = 5
print(x > 3 or x < 4)#or

x = 5
print(not(x > 3 and x < 10))#not

#identity operators
#is
x = ["yashu", "nandu"]
y = ["yashu", "nandu"]
z = x
print(x is z)
print(x is y)
print(x == y)

#is not
x = ["yashu", "nandu"]
y = ["yashu", "nandu"]
z = x
print(x is not z)
print(x is not y)
print(x != y)


#membership operators

x = ["yashu", "nandu"]
print("nandu" in x)#in

x = ["yashu", "nandu"]
print("kavya" not in x)#not in


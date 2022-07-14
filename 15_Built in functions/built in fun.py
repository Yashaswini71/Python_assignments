'''abs:The abs() function returns the absolute value of the specified number.'''
#Syntax:
#abs:
'''abs(n)'''

x = abs(-7.25)
print(x)


#Syntax:
#all(iterable)

'''all:The all() function returns True if all items in an iterable are true, otherwise it returns False.
If the iterable object is empty, the all() function also returns True.'''

mylist = [True, True, True]
x = all(mylist)
print(x)


'''The any() function returns True if any item in an iterable are true, otherwise it returns False.
If the iterable object is empty, the any() function will return False.'''
#syntax:
#any
'''any(iterable)'''

#example:
mytuple = (0, 1, False)
x = any(mytuple)
print(x)                 # Returns True because the second item is True


'''The bin() function returns the binary version of a specified integer.
The result will always start with the prefix 0b.'''

#syntax
#bin
'''bin(n)'''

#example
x = bin(36)
print(x)                 # The result will always have the prefix 0b


'''The bytearray() function returns a bytearray object.
It can convert objects into bytearray objects, or create empty bytearray object of the specified size.'''

#syntax

#byte array

#example

x = bytearray(4)
print(x)

'''The format() function formats a specified value into a specified format.'''

#syntax:
'''format(value, format)'''

x = format(0.5, '%')
print(x)












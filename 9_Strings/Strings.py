my_string = 'yashu'
print(my_string)

my_string = "yashu"
print(my_string)

my_string = '''yashu'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """hi, learning python"""
print(my_string)

#Accessing string characters in Python
str = 'programiz'
print('str = ', str)

print('str[0] = ', str[0])  #first character

print('str[-1] = ', str[-1])          #last character

print('str[1:5] = ', str[1:5])        #slicing 2nd to 5th character

print('str[5:-2] = ', str[5:-2])      #slicing 6th to 2nd last character

#Concatenation of Two or More Strings

# Python String Operations
str1 = 'Hello'
str2 ='World!'

print('str1 + str2 = ', str1 + str2)   # using +

print('str1 * 3 =', str1 * 3)          # using *


# Iterating through a string

count = 0
for letter in 'yashaswini':
    if(letter == 'a'):
        count += 1
print(count,'letters found')

#Built-in functions 

str = 'yashu'
list_enumerate = list(enumerate(str))             # enumerate()
print('list(enumerate(str) = ', list_enumerate)
print('len(str) = ', len(str))                    #character count

#upper()
a = "I am yashaswini"
x = a.upper()
print(x)                  #Converts a string into upper case


#lower()
txt = "I AM YASHASWINI"
x = txt.lower()
print(x)                   #Converts a string into lower case

#join()

s=(['This',   'will',   'join',   'all',   'words',   'into',   'a',   'string'])
x = ' '.join(s)

print(x)

#The format() Method for Formatting Strings

# default(implicit) order
first_order = "{}, {} and {}".format('yashu','nandu','divya')
print('\n--- first Order ---')
print(first_order)

# order using positional argument
second_order = "{1}, {0} and {2}".format('yashu','nandu','divya')
print('\n--- second Order ---')
print(second_order)

# order using keyword argument
third_order = "{s}, {b} and {j}".format(j='yashu',b='nandu',s='divya')
print('\n--- third Order ---')
print(third_order)

#Examples:
#Strings

str1="python"
print("str1:",id(str1))
str2="python"
print("str2:",id(str2))
str1=str1+str2 #immutable
print("str1:",id(str1))

#index
s="python"
print("s[0]:",s[0])
print("s[1]:",s[1])
print("s[2]:",s[2])
print("s[3]:",s[3])
print("s[4]:",s[4])
print("s[5]:",s[5])
print("s[-1]:",s[-1])
print("s[-2]:",s[-2])
print("s[-3]:",s[-3])
print("s[-4]:",s[-4])
print("s[-5]:",s[-5])
print("s[-6]:",s[-6])

#slicing
s="python"
print(s[1:4])
print(s[1:])
print(s[:4])
print(s[:])
print(s[-4:-2])
print(s[-5:4])
print(s[1:4:2])
print(s[-1:6:-2])


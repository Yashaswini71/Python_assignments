#data types

'''
text type     : str

Numeric Types : int,float,complex

Sequence Type : List,tuple,range

Mapping Types : dict

Set Types     : set,frozenset

Boolean Type  : bool

Binary Type   : bytes,bytearray,memoryview

None Type     : Nonetype
'''

#Examples:

#print the data type of the variables 
#Text type

x="helloworld"
print(type(x)) #str

#Numeric type:

x=5
print(type(x)) #int

y=2.5
print(type(y)) #float

z=2j
print(type(x)) #complex

# types of conversions:

x = 1          # int
y = 2.8        # float
z = 1j         # complex
a = float(x)   #convert from int to float:
b = int(y)     #convert from float to int:
c = complex(x) #convert from int to complex:
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Sequence Types:

x=["yashu","nandu","kavya"] # list
print(x)                    # display x:
print(type(x))              # display the data type of x:

x=("yashu","nandu","kavya") # tuple
print(x)                    # display x:
print(type(x))              # display the data type of x:

x= range(7)                 #range
print(x)                    # display x:
print(type(x))              # display the data type of x:

#Mapping Types:

x = {"Game" : "Volleyball", "since" : 8} #dict
print(x)                    # display x:
print(type(x))              # display the data type of x:

#Set Types:

x = {"apple", "banana", "cherry"} # set
print(x)                    # display x:
print(type(x))              # display the data type of x:

x = frozenset({"apple", "banana", "cherry"}) # frozenset
print(x)                    # display x:
print(type(x))              # display the data type of x:

#Boolean Type:
x = True                    # bool
print(x)                    # display x:
print(type(x))              # display the data type of x:

# Binary Types:
x = b"Hello"                # bytes
print(x)                    # display x:
print(type(x))              # display the data type of x:

x = bytearray(5)            #bytearray
print(x)                    # display x:
print(type(x))              # display the data type of x:

x = memoryview(bytes(5))    #memoryview
print(x)                    # display x:
print(type(x))              # display the data type of x:

x = None                    #NoneType
print(x)                    # display x:
print(type(x))              # display the data type of x:

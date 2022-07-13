# Different types of sets in Python

# set of integers
num= {1, 2, 3}
print(num)

# set of mixed datatypes
mixed = {1.0, "Hello", (1, 2, 3)}
print(mixed)

# set cannot have duplicates

my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set)

# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))            #dictionary

# initialize a with set()
a = set()

# check data type of a
print(type(a))              # set


# initialize my_set
my_set = {1, 3}
print(my_set)

# add an element

my_set.add(2)
print(my_set)

# add multiple elements

my_set.update([2, 3, 4])
print(my_set)

# add list and set

my_set.update([4, 5], {1, 6, 8})
print(my_set)

# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)          # use | operator

# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A & B)           # use & operator

# methods

#copy syntax
'''set.copy()'''

# Examples
numbers = {1, 2, 3, 4}

# copies the items of numbers to new_numbers
new_numbers = numbers.copy()

print(new_numbers)

# set syntax
'''set.add(elem)'''

#Examples

a = {2, 3, 5, 7}
a.add(11)         # add 11 to a
print(a)







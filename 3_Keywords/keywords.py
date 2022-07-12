#keywords:

#And -a logical operators

x = (5 > 3 and 5 < 10) 
print(x)                #true

#break:

for i in range(9):
  if i > 3:
    break
  print(i)

# class:

class Person:
  name = "John"
  age = 36
print(Person.name)

# Continue
 
for i in range(9):
  if i == 3:
    continue
  print(i)

# def

def my_function():
  print("Hello from a function")

my_function()

# del

x = "hello"
del x
print(x)

#elif

for i in range(-5, 5):
  if i > 0:
    print("YES")
  elif i == 0:
    print("WHATEVER")
  else:
    print("NO")

# else

x = 2
if x > 3:
  print("YES")
else:
  print("NO")

# global

def myfunction():
  global x
  x = "hello"

myfunction()
print(x)

# return

def myfunction():
  return 3+3

print(myfunction())


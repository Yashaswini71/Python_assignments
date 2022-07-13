#control structure

'''
syntax :
for i in range():
    statement
    
for i in list:
    statement
    
for i in string:
    statement
    
'''

#Examples
str = "hello world"
for i in str:
    print(i,end=' ')
print()
    
for i in range(5):
    print(i,end = ' ')
print()

for i in range(20,22,3): 
    print(i,end=' ')
print()
print()

arr = [1,2,"hello","hi",20,22,3]
print("This is a list: ",end=' ')
for i in arr:
    print(i,end=' ')
print('\n')

arr = (1,2,3,4,5,"hello",6.3)
print("This is a tuple: ",end=' ')
for i in arr:
    print(i,end=' ')
print('\n')

#syntax :

'''if condition:
    statement
    statement
elif condition:
    statement
    statement
else:
    statement
'''

num = int(input("Enter the value "))
print("You entered {0}".format(num))

if num>0 and num <=20:
    print("You are in low band")
elif num >20 and num <=30:
    print("You are in medium band")
elif num>30:
    print("You are in high band")
else:
    print("You entered an invalid value")
    
    
#syntax:
'''while condition:
    statement
    statement'''


#Example

num = 5
while num>0:
    print(num)
    num ==1
    

#selection

x=5
if x > 0:
    print("x is +ve")


if x>0:
    print("x is +ve")
else:
    print("x is not +ve")
         
x=int(input())
if x >0:
    print("x is +ve")
elif x<0:
    print("x is -ve")
else:
    print("x is 0")
            
#iteration(loops)

for x in ["c","c++","python"]:
    print(x)
a=10
while a>0:
    print("a is:",a)
    a=a-2
    
        
#Range()

for a in range(3):
    for b in range(3):
        print(a,b)


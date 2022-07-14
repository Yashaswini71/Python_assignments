#Write a program to display the largest word from the string

str=input("Enter any String :")
L = str.split()
max=0
b=""
for i in L:
     if len(i) > max:
           b=i
           max=len(i)
print("Longest word is ",b)

#Write a program to accept a string and count the frequency of each vowel.

str1=input("Enter String :")
print("frequency of vowel 'a' is :",str1.count('a'))
print("frequency of vowel 'e' is :",str1.count('e'))
print("frequency of vowel 'i' is :",str1.count('i'))
print("frequency of vowel 'o' is :",str1.count('o'))
print("frequency of vowel 'u' is :",str1.count('u'))


#print the below pattern
'''
*
* *
* * *
* * * *
* * * * *
'''

rows = int(input('Enter the number:'))

for i in range(0,rows):
    for j in range(0,i+1):
        print("* ",end="")
    print()

#program to check if the entered number is even or odd

num = int(input('Enter the number:'))

if(num % 2 == 0):
    print("{0} is an even number".format(num))
else:
    print("{0} is an odd number".format(num))


#program to find the sum of N natural numbers

num = int(input('Enter the number:'))

sum_num = 0

for i in range(1,num+1):
    sum_num = sum_num + i

print('Sum of {0} natural numbers is: {1}'.format(num,sum_num))



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

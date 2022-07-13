# Lists are used to store multiple items in a single variable

#list

#mutable
a=[1,2,3]
id(a)

a[1]=10
print(a)
id(a)

#linear data structure
a=[1,2,3]
a=a+[4,5]
print(a)

#mixed type elements
a=[1,"hi",20.5]
print(a)

#zero based indexing
a=[10,20,30,40]
a[0]
print(a)

#nested list
a=[10,20,[1,2,3],30]
print(a)

#len()
print(len([10,20,30,40]))

#concatenation
print([10,20]+[15,25])

#repetition
print(['python']*3)
['python', 'python', 'python']
print(3 in[1,2,3])#membership
print(3 in[1,2,3])
print(3 in[1,2,4])
for x in[1,2,3]:#iteration
    print(x*x)

#list indexing
s=['p','Y','T','H','O','N']
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

#list slicing
s=[10,20,30,40,50]
print(s[1:4])
del(s)#deleting list

    

#list methods
#append()
a=[1,2,3]
a.append(4)
print(a)

#extend()
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

#insert()
a=[10,20,30]
a.insert(1,40)
print(a)

#sort
a[50,20,40,30]
a.sort()
print(a)

#reverse()
a=[10,20,30,40,50]
a.reverse()
print(a)

#all()
a=[1,0,1]
print(all(a))

#any()
a=[1,0,0,1]
print(any(a))

#enumerate
a[11,22,33]
print(list(enumerate(a)))

#list()
s="abcdef"
print(list(s))

#min()
a=[11,22,33,44,55]
print(min(a))

#sum()
a=[11,22,33,44,55]
print(sum(a))


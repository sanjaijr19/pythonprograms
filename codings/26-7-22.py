#1 odd items in list
x=[1,2,3,4,5,5,6,6,7,7,8,8,8]
for i in x:
    if (i%2)!=0:
        print(i,end=" ")

#2 multiply all elements in list
x=int(input("enter the number"))
y=1
for i in str(x):
    y=y*int(i)
print(y)


#3 print aa listin nested list
q=[["red"],["blue"],["green"]]
print("\n".join([str(lst) for lst in q]))

#4
x=["fruits","vegetables","juice"]
y=["apple","potato","mango"]
for u,v in zip(x,y):
    print({"type:",u})
    print({"name:",v})

#5
x=["a","b","c","d","e","f","g","h","i","j","k"]
print(x[::2])
print(x[1::2])


#6 find all values in the list greater than specified value
list1=[123,423,44,654]
list2=[131,245,767]
print(all(x>200 for x in list1))
print(all(x>100 for x in list2))

#7 join a list
a=["red","blue","green"]
print("-".join(a))
print("".join(a))

#8 covert string to list
b="sanjaikumar","python"
c=list(b)
print(c)

#9 add two list
x=[1,2,4,5,6,7,8,9,3]
y=[2,4,6,8,9,10]
x.extend(y)
print(x)

#10 Write a Python program to check whether the n-th element exists in a given list.
x=[1,3,2,4,5,6,8,9,7]
print("total length of list is ",len(x))
print("the last element is ",x[-1])


#11 Write a Python program to insert a given string at the beginning of all items in a list.
x=[1,2,3,4]
for i in x:
    print("emp{}".format(i))

#12 Write a Python program to iterate over two lists simultaneously.
x=["red","green","yellow"]
y=[1,2,3]
for i,j in zip(y,x):
    print(i,j)

#13 Write a Python program to extend a list without append.
x=[1,2,3,43,4,5]
y=[2,3,4,5,5,43,7,8,9]
z=x+y
x=y
print(z)
print(x)

#14 Write a Python program to print a list of space-separated elements.
a=[1,2,3,4,5,6]
print(*a)



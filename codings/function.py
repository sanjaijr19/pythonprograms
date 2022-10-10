#1 find largest number among three numbers
def largest(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
largest(2,4,5)


#2 sum all the number in  list
def sum(n):
    sum=0
    for i in n:
        sum=sum+i
    return sum
#m=int(input("enter the number"))
print(sum([1,2,3,4]))

#3 multiply all the number in list
def mul(a):
    mul=1
    for j in a:
        mul=mul*j
    return mul
print(mul([1,2,3,4]))

#4 reverse a string
def rev(s):
    s=s[::-1]
    return s
s=input("enter the string")
print(rev(s))


#5 function that takes list and return a new list with unique element of the first list
def list(x):
    y=[]
    for i in x:
        if i not in y:
            y.append(i)
    return y
print(list([1,2,3,4,5,6,7,7,7,6,5,4,3,2,1]))


x="sanjaikumar"
y=x.upper()
print(y)
print(len(y))
z=x.lower()
print(z)
print(len(z))
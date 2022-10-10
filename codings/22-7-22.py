#1Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
x=input("enter the string")
y=0
z=0
for i in x:
    if (i.islower()):
        y=y+1
    elif (i.isupper()):
        z=z+1
print("the number of lowercase", y)
print("the number of uppercase",z)

#2  Write a Python program to access a function inside a function.
def main(x,y):
    print(x+y)
    def sum(a,b):
        return a+b
    print(sum(1,2))
main(3,4)


#3   Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.\
# If the string length is less than 2, return instead of the empty string.
def function(x):
    if len(x)<2:
        return ''
    return x[0:2]+x[-2:]
print(function("sanjai"))

#4   Write a Python program to construct the following pattern, using a nested for loop.
row=int(input("enter the no of rows"))
for i in range(0,row):
    for j in range(0,i+1):
        print("*",end="")
    print()
for i in range(row+1,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print()
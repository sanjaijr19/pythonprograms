#1 First 10 Even numbers
print("the first 10 even numbers")
for i in range(1,21):
    if i%2==0:

        print(i)
#2 First 10 Odd numbers

print(" the first 10 odd numbers")
for i in range(1,21):
    if i%2!=0:
        print(i)
#3  Write for loop statement to print the following series:
#   10, 20, 30 … … 300
for j in range(1,301):
    if j%10==0:
        print(j)
#4 Write a program to print first 10 integers and their squares like
for k in range(1,11):
    print("the square root of",k)
    m=k**2
    print(" is ",m)

#5Write a for loop statement to print the following series
#105, 98, 91 ………7
for x in reversed(range(7,106)):
    if x%7==0:
        print(x)

#6  Write a program to print all the factors of a number using for loo
t=int(input("enter the number"))
for s in range(1,t+1):
    if t%s==0:
        print("the factors are",s)
#7  First 10 Natural numbers
print("the first 10 natural numbers is")
for i in range(1,11):
    print(i)
#8 First 10 Whole numbers
print("the first 10 whole numbers is ")
for i in range(0,11):
    print(i)

#9 Write a program to find the sum of the digits of a number accepted from the user.
n=int(input("enter the number"))
sum=0
for i in str(n):
    sum=sum+int(i)
print(sum)

#10 Write a program to display all even numbers that falls between two numbers
# (exclusive both numbers) entered from the user.
a=int(input("enter the first number"))
b=int(input("enter the second number"))
for i in range(a,b+1):
    if (i%2)==0:
        print(i)
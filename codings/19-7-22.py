#1 check whether the given number is leap year or not.
x=int(input("enter the year"))
if (x%4)==0:
    print(x,"is leap year")
else:
    print((x,"is not leap year"))

#2 Python program to print all even numbers in given range
for i in range(1,21):
    if i%2==0:
        print(i)

#3	Python program to print grades based on marks scored by a student
mark=int(input("enter the mark"))
if mark>90:
    print("Grade O")
elif mark >= 80 and mark <90:
    print("Grade A+")
elif mark >=70 and mark <80:
    print("Grade A")
elif mark >=60 and mark <70:
    print("Grade B+")
elif mark >=50 and mark <60:
    print("Grade B")
else:
    print("Grade F")



#4 Python program to print Fibonacci numbers to given limit
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==0:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(10)

#5 Python program to print list in reverse order
x = [1, 2, 3, 5, 6, 7, 8, 5, 3]
x.reverse()
print("the reverse order of the list is", x)
y=["p","y","t","h","o","n"]
y.reverse()
print("the reverse order of the list is",y)

#6 Python program to print numbers from 1 to n except 5 multiples
for n in range(1,51):
    if n % 5 != 0:
        print(n)

#7 Have a function that accepts a country name and return its capital using If…Else
countryname = input("enter the country name")
if countryname in ("India","England","France"):
    print("the capital is ")
else:
    print("no data found")
if countryname=="India":
    print("New Delhi")
elif countryname=="England":
    print("London")
elif countryname=="France":
    print("Paris")
else:
    print("please try again")











































































































































































































































































































































































































































































































































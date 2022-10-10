# print("hello")
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
#
# print("1.addition")
# print("2.subraction")
# print("3.multiplication")
# print("4.division")
#
# while True:
#     choice=input("enter your choice(1/2/3/4)")
#
#     if choice in ("1","2","3","4"):
#         num1=float(input("enter the first number"))
#         num2=float(input("enter the second number"))
#         if choice=="1":
#             print(add(num1,num2))
#         elif choice=="2":
#             print(sub(num1,num2))
#         elif choice=="3":
#             print(mul(num1,num2))
#         elif choice=="4":
#             print(div(num1,num2))
#
#import datetime

#
# def lar(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# print(lar(23,45))
#
#
# def rev(a):
#     return a[::-1]
# print(rev("sanjai"))
#
# #n=int(input("enter the number"))
# n=7
# f=1
# for j in range(2,n+1):
#     f*=j
# print(f)
#
# def myfunc(*args):
#     print("my name is ",args[0])
# myfunc("sanjai","kumar")
#
# def func(**kids):
#     print("my chid is ",kids["kids1"])
# func(kids1="tom",kids2="jerry")
#
#
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=5
# print(factorial(n))
#
# n=input("enter the letter")
# if n[::1] == n[::-1]:
#     print(n,"is palindrome")
# else:
#     print(n," is not a palindrome")
#

def outer_func():
    x = 777

    def inner_func():
        # local variable now acts as global variable
        nonlocal x
        x = 700
        print("value of x inside inner function is :", x)

    inner_func()
    print("value of x inside outer function is :", x)

outer_func()


x=lambda a,b,c:a*b*c
print(x(6,3,4))


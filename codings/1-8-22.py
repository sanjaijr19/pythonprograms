# print("helo")
# var=40
# for i in range(20):
#     for j in range(2,10,1):
#         if var%2==0:
#             continue
#         var+=1
#     var+=1
# else:
#     var+=1
#     print(var)
#
# for l in 'Jhon':
#    if l == 'o':
#       continue
#    print(l, end=", ")
#
# print(type(0xFF))
#
#
# print(dict())
#
#
#
#
#
# x=6
# y=2
# print(x**y)
# print(x//y)
#
#
# print(type(123))
#
# print(0x1F)
# print(bin(2))
# print(0o10)
#
# num=tuple({1:"one",2:"two"})
# print(num)
#
# for i in range(3,-5,-2):
#     print(num,end="")
#
#
# items=["milkshake","smoothie"]
# items1=["banana","apple"]
# for y in items:
#     for x in items1:
#         print(x,y)
#
# sampledict=dict([
#     ("first",1),
#     ("second",2),
#     ("third",3)
# ])
# print(sampledict)
#
#
# str1="my isname isisis jameis isis bond"
# sub="is"
# print(str1.count(sub,4))
#
#
# dict1={"name":"mike","salary":2000}
# temp=dict1.get("age")
# print(temp)
#
# x=-5j
# print(type(x))
#
# l=[None]*10
# print(len(l))
#
# print(0b101)
# print(0o10)
# print(0x1FF)
#
# print(str(hello))
#
# def hello(a):
#     x="hello"
#     return x
# print(hello("x"))
#
#
# def myfunc(name,place):
#     print(f"my name is {name},i am from {place}")
# myfunc("sanjai","tanjore")
#
# def display(**kwargs):
#     for i in kwargs:
#         print(i)
#
#
# def add(a,b):
#     return a+b
# print(add(4,3))
#
#
# def odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# odd(10)
#
# def loop(x):
#     for i in x:
#         print(i)
# loop("sanjai")
#
# def bio(name,age):
#     print("my name is ", name,"my age is",age,)
# bio("sanjai",20)
#
#
#
#
#
# for i in range(1,11):
#     z=i**2
#     print(z)
#
#
# def sqrt(n):
#     for i in range(4,31):
#         return i**2
# print(sqrt(i))
#
# c=87
# f=(((c+32)+5)/9)
# print(f)
#
#
# n=int(input("enter the number"))
# if res>1:
#     res=((n*(n+1))/2)
#     print(res)


n=int(input("enter the number"))
for i in range(1,n+1):
        res=((i*(i+1))/2)
        print(int(res))


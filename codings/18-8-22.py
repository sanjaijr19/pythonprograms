# #1
# n=int(input("enter the number greater than 10"))
# while True:
#     if n<11:
#         print("please enter the number above 10!")
#
#     for i in range(1,n+1):
#         if (i%2)!=0:
#             print(i)
#     break
# print("\n")
#
# #2
# num=int(input("enter the number greater than 10"))
# while True:
#     if num<11:
#         print("please enter the number above 10!")
#         break
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
#     break
#
# print("\n")
#
# #3
# m=int(input("enter the number"))
# n=int(input("enter the count"))
# for i in range(1,n+1):
#     print(m,"*",i,"=",m*i)
#


# n=int(input("enter the number"))
# while True:
#     if n==0:
#         print("enter the number greater than 0")
#         break
#
#     sum=0
#     count=0
#     while count<n:
#         num=int(input("enter the value"))
#         sum+=num
#         count+=1
#     avg=sum/n
#     print(avg)
#     break
#
# x=input("enter the string")
# #
# if x[::1] == x[::-1]:
#     print(x,"is palindrome")
# else:
#     print(x,"not a palindrome")
#


x=lambda:"Even Number"if 4%2==0 else"Odd Number"
print(x())

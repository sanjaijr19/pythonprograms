# #1 swapping two variable without temporary variable
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# print("a=",a)
# print("b=",b)
# a=a+b
# b=a-b
# a=a-b
# print("value after swapping \n a=",a)
# print("value after swapping \n b=",b)
#
#
#
#
# #2 check anagram
# def check(x,y):
#     if sorted(x)==sorted(y):
#         print("given strings are anagram")
#     else:
#         print("given strings are not anagram")
# x=input("enter the string")
# y=input("enter the string")
# check(x,y)
#
# #SiLeNtCAT
# #LisTenAcT
#
# #3 reverse a each word in string
# s=input("enter the sentence")
# t=s.split()
# r=[]
# for i in t:
#     r.append(i[::-1])
# u=" ".join(r)
# print(u)
#
# #4 print all substring of a string
# a=input("enter the string")
# for i in range(len(a)):
#     for j in range(i+1,len(a)+1):
#         print(a[i:j])
#
#
# #6 number pattern
# rows=int(input("Enter number of rows: "))
# k=0
# count=0
# count1=0
# for i in range(1,rows+1):
#     for j in range(1,(rows-i)+1):
#         print("  ",end="")
#         count+= 1
#     while k!=((2*i)-1):
#         if count<=rows-1:
#             print(i+k,end=" ")
#             count+=1
#         else:
#             count1+=1
#             print(i+k-(2*count1),end=" ")
#         k+=1
#
#     count1=count=k= 0
#     print()
#
# #7
# lines=5
# i=1
# while(i<=lines):
#     j=lines
#     while j>=1:
#         if j!=i:
#             print(j,end=" ",flush=True)
#         else:
#             print("*",end=" ",flush=True)
#         j=j-1
#     print()
#     i=i+1
#
# #8 number of occurence of string
# x="pythonprogramming"
# y=x.count("p")
# print(y)
#


# 1.number of occurence of each character in string
n=input("enter the string")
freq={}
for i in n:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)





#2.print letter E in star
height=5
def printE():
    for i in range(0,height):
        print("*",end=" ")
        for j in range(0,height):
            print("*",end=" ")
            if ((i==0 or i==height-1) or (i==height//2 and j<=height//2)):
                print("*",end=" ")
            else:
                break
        print()
printE()


#3.print letter F in star
height=5
def printF():
    for i in range(0,height):
        print("*",end="")
        for j in range(0,height):
            if ((i==0) or (i==height//2 and j<=height//2)):
                print("*",end="")
            else:
                continue
        print()
printF()



#4.print letter O in star
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and (i!=0 and i!=6)) or ((i==0 or i==6) and (j>0 and j<4)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()


# 5.Reverse a string preserving space positions
def reverses(st):
    n = len(st)
    result =[0]*n
    for i in range(n):
        if (st[i]== ' '):
            result[i]=' '
    j=n-1
    for i in range(len(st)):
      if(st[i]!=' '):
            if(result[j]==' '):
                j-=1
            result[j]=st[i]
            j-=1
    return ''.join(result)
if __name__ == "__main__":
    st = input("enter the strings to be reverse")
    print(reverses(st))

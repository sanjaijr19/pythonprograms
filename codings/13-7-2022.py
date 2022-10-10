#arithmetic operator
#addition
x=5
y=16
print(x+y)

#subraction
#x=int(input("enter the number"))
#y=int(input("enter the number"))
#print(x-y)

#multiplication
x=23
y=21
print(x*y)

#division
#x=int(input("enter the number"))
#y=int(input("enter the number"))
#print(x/y)
#modulus(remainder)
#print(x%y)


#x=int(input("enter the number"))
#y=int(input("enter the number"))
#print(x+y)
#print(x-y)
#print(x*y)
#print(x/y)
#print(x%y)



#exponential
x=4
y=3
print(x**y) #(4*4*4)=64

#floor division
x=8
y=5
print(x//y)  #(get nearest whole number in division method)

#assignment operator
x=5
x+=10  #(x=x+5)
print(x)

y=18
y-=20 #(y=y-20)
print(y)

z=6
z*=10 #(z=z*10)
print(z)

a=15
a/=5 #(a=a/5)
print(a)

b=10
b %= 5  #(b=b%5)
print(b)

c=4
c//=5  #(c=c//5)
print(c)

d=5
d**=5
print(d)




#comparison operator
e=9
f=10
print(e==f) #(it will return true or false)
print(e!=f)
print(e>f)
print(e<f)
print(e>=f)
print(e<=f)

#logical operator
j=10
print(j<15 and j>5) #(It is true when both condition satisfies)

i=5
print((i<=5 or i>10)) #(It is true when any one condition satisfies)

k=8
print(not(k>4 and k<10)) #(reverse the output,if the condition is true it will be false)

#membership operator
x=["sanjai","kumar"]
print("sanjai" in x)
print("python" not in x)


#Datatypes
x=str("sanjai") #(denotes word)
print(x)
print(type(x))

y=int(20) #(denotes number)
print(y)
print(type(y))

z=float(1.4) #(denotes decimal number)
print(z)
print(type(z))

a=["python","java","html"] #(list must be in square brackets)
print(a)
print(type(a))

b=tuple(("python","java","html")) #(tuple must be  in closed brackets)
print(b)
print(type(b))

c=set(("python","java","html")) #(sets must be in {})
print(c)
print(type(c))

d=dict(brand="honda",year="1998")
print(d)
print(type(d))

e=range(7)
print(e)
print(type(e))

f=complex(3j)
print(f)
print(type(f))

i=bool(5)
print(i)
print(type(i))

j=bytes(5)
print(j)
print(type(j))

k=memoryview(bytes(8))
print(k)
print(type(k))

#list
x=["apple","mango","guava","banana","watermelon"]
print(x[1])
print(x[2:5])
x[1]="orange"
print(x)
x[2:4]=("strawberry","litchie")
print(x)
x.append("orange")
print(x)
x.insert(1,"lemon")
print(x)

a=["apple","mango","guava","banana","watermelon"]
b=["strawberry","litchie"]
a.extend((b))
print(a)
a.remove("apple")
print(a)
b.pop()
print(b)
a.clear()
print(a)
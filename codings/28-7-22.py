x=(1,2,3,4,5)
y=1
for i in x:
      y=y*i
print(y)


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4={}
for d in (dic1,dic2,dic3):
      dict4.update(d)
print(dict4)


x={"name":"sanjai","age":20}
for i,j in x.items():
      print(i,"->",j)


x=int(input("enter the number"))
d=dict()
for i in range(1,x+1):
      d[i]=i*i
print(d)


d=dict()
for x in range(1,16):
      d[x]=x**2
print(d)


x1={"x":21,"y":24}
x2={"z":12,"A":34}
x=x1.copy()
x.update(x2)
print(x)

x=("name","age","dob")
y=("sanjai")
z=dict.fromkeys(x,y)
print(z)


print(dict([("sanjai",19),("kumar",18)]))


x=(("sanjai",19),("kumar",18))
y=dict(x)
print(y)
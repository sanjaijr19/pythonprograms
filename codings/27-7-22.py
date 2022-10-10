# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# print(list1[2][1][2][1])
#
# x=["sanjai","python"]
# y=["kumar","programming"]
# for i,j in x,y:
#     print(i,j)
#
#
# a=(100)
# print(a*2)
# print(type(a))
#
# b=("orange")
# print(type(b))
# a=("Orange")
# print(type(a))


x=55
y=45
x,y=y,x
print(x,y)

a=(("a",2),("d",4),("a",6),('b',6))
b=(sorted(list(a),key=lambda x:x[1]))
print(tuple(b))

q=("s","a","n","j")
p="".join(q)
print(p)

x=((0,1,2),(2,3,4),(5,6,7))
for i in x:
    y=i[:-1]+(100,)
    print(y)

a=(("a","b"),("c","d"),(),(""),(""))
for j in a:
    if j:
        print(j)

x=((12,34),(45,67),(78,9))
for i in x:
    y=sum(i)
    print(y/2)


a=(1,2,3,4)
b=(2,4,6,8)
c=(1,3,5,7)
d=map(sum,zip(a,b,c))
print(tuple(d))

s=[(1, 2), (2, 3), (3, 4)]
print(list(s))
print(list(s))



l=(11,11,11,23,2,33,55)
k=l.count(11)
print(k)

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))


def check(t):
    return all(i == t[0] for i in t)

#tuple1 = (45, 45, 45, 45,88)
print(check((4,12,54,14,88)))

# def check(x):
#     return
# for i in x:
#     y=all(i==x[0])
# print(check(21,13,33))
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45,88)
print(check(tuple1))



x=["chennai","mumbai","bangalore"]
y=[i for i in x if "v" in i]
print()
int(y)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

z=["sanjai","kumar"]
t=[w.upper() for w in z]
print(t)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['sanjai''kumar' for x in fruits]

print(newlist)
x=["apple","mango","banana"]
x.sort(key=str.upper())
print(x)

x=["dog","cat","lion","tiger"]
y=["sanjai" for i in x]
print(y)

x=[y for y in range(15) if y>5]

print(x)0
x=["dog","cat","lion","tiger"]
y=[z if z!="cat" else "sanke" for z in x]
print(y)

x=["dog","cat","lion","tiger"]
x.sort(reverse=False)
print(x)

x=["apple","banana","mango"]
x.sort(key=str.lower())
print(x)

x=["apple","banana","mango"]
x.reverse()
print(x)


x=("apple","banana","mango")
y=list(x)
y[1]="grapes"
x=tuple(y)
print(x)

x=("apple","banana","mango")
y=("guava",)
x+=y
print(x)

x=("apple","banana","mango")
y=list(x)
y.remove("banana")
x=tuple(y)
print(x)



x=("apple","banana","mango")
(red,yellow,green)=x
print(red)
print(yellow)
print(green)

x=("apple","banana","mango","watermelon")
(*red,yellow,green)=x
print(red)
print(yellow)
print(green)

x={"apple","banana","mango","watermelon"}
y=x.pop()
print(y)
print(x)

x={"brand":"benz","model":"gf23","year":1996}
print(x["model"])
print(type(x))
y=x.keys()
print(y)
z=x.values()
print(z)
x["brand"]="audi"
print(x)
x["colors"]="red"
print(x)
w=x.items()
print(w)
x.update({"year":2000})
print(x)
x.pop("year")
print(x)
x.popitem()
print(x)
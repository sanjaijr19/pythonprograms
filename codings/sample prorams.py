
x=input("enter the string")
y=0
for i in x:
    y=y+1
    z=(x[0:2]+x[y-2:y])
print(z)

def strings(x):
    y=0
    for i in x:
        if len(i)>1 and i[0]==i[-1]:
            y+=1
    return y
print(strings(["aba","ase","qwe","yju","sds","99876","989769"]))

a={"name":"sanjai","year":2000,"place":"mannargudi"}
a['place']="tanjore"
print(a)
a["food"]="briyani"
print(a)
a.pop("place")
print(a)
a.popitem()
print(a)
for i in a:
    print(i)
b=a.get("name")
print(b)
c=a.keys()
print(c)
d=a.values()
print(d)
for j in a.values():
    print(j)
for k in a.keys():
    print(k)
l=a.copy()
print(l)
h=dict(a)
print(a)
sanjai={"food1":{"chat":"panipuri","desserts":"icecream"},"food2":{"fruits":"apple","juices":"mango"}}
print(sanjai)
f=sanjai.keys()
print(f)
g=sanjai.values()
print(g)
sanjai["food1"]="food3"
print(sanjai)
sanjai.update({"food1":"briyani"})
print(sanjai)

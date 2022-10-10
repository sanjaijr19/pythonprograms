n=int(input("enter the number"))
for i in range(2,n):
    if (n%i)==0:
        print("not prime number")
        break
    else:
        print("prime number")
        break

class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def student(self):
        x=f"{self.fname}{self.lname}"
        return x


class people:
    pass
a=person("sanjai","kumar")
print(a.student())



class addition:
    def add(self):
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        c=a+b,a-b,a/b,a*b
        print(c)
class subraction(addition):
    def sub(self):
        a = int(input("enter the number"))
        b = int(input("enter the number"))
        d = a - b
        print(d)
obj=subraction()
obj.add()
obj.sub()


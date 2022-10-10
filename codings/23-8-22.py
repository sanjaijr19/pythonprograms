class Student:
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name
student = Student('V12', 'Frank Gibson', 'V')
print(student.student_id)


class A:
    def __init__(self,name):
        self.name=name
a1=A("john")
a2=A("john")
print(a1.name)
print(a2.name)

set1={"a",3,"b",3}
print(set1)

class Person:
    def __init__(self, id):
        self.id = id



class A:
    def __init__(self, i = 0):
        self.i = i

class B(A):
    def __init__(self, i = 3):
        self.i = i

def main():
    b = B()
    print(b.i)
    print(b.i)

main()

sam = Person(100)

sam.__dict__['age'] = 49

print ( len(sam.__dict__))



# class student:
#     def __init__(self,name="sanjai",age=98,place="mannargudi"):
#         self.name=name
#         self.age=age
#         self.place=place
# class teacher(student):
#     def mark(self,name,age):
#         student.name=name
#         student.age=age
#         r=f"name={self.name} \n age={self.age}"
#         return r
# obj=teacher()
# print(obj.mark())


class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def mass(self):
        return self.length/self.breadth
class rectangle(shape):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)
    def volume(self):
        return self.length*self.breadth
class cube(shape):
    def __init__(self,length,breadth,height):
        super().__init__(length,breadth)
        self.height=height
    def area(self):
        return self.length*self.breadth*self.height
obj=cube(1,2,9)
print(obj.area())
obj1=rectangle(4,6)
print(obj1.volume())
obj3=shape(5,4)
print(obj3.mass())
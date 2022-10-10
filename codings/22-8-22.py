class student:
    def __init__(self,name,age,place):
        self.name=name
        self.__age=age
        self._place=place
    def bio(self):
        r=f"name={self.name}\nage={self.__age}\nplace={self._place}"
        return r
obj=student("sanjai",22,"thanjavur")
print(obj.bio())

#
# class people:
#     def __init__(self,mark1,mark2,mark3):
#         self.__mark1=mark1
#         self.__mark2=mark2
#         self.__mark3=mark3
# b=people(90,34,56)
# print(b.__mark1)
#
print(5+2*8/2)
import django
print(django)
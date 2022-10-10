import calendar


class student:
    def __init__(self,name,age,dob,city,country):
        self.name=name

        self.age=age
        self.dob=dob
        self.city=city
        self.country=country
    def address(self):
        addr=f"name:{self.name}\nage:{self.age}\ndob:{self.dob}\ncity:{self.city}\ncountry:{self.country}"
        return addr

stu1=student("sanjaikumar",21,2000,"mannargudi","India")
print(stu1.address())


from _datetime import datetime
print(datetime.now())




class person:
    def __init__(self,name,place,gender,dob):
        self.name=name
        self.place=place
        self.gender=gender
        self.dob=dob
    def address(self):
        add=f"name:{self.name}\nplace:{self.place}\ngender:{self.gender}\ndob:{self.dob}"
        return add
p1=person("robert","USA","male",1985)
print(p1.address())

x="sanjai"
y="18"
print(type(y))


import calendar
print(calendar.month(2000,8))


class people:
    def __init__(sanjai,name,marks):
        sanjai.name=name
        sanjai.marks=marks
class person(people):
    pass
po1=person("sanjai",88)
po2=person("dhoni",99)
print(po1.name)
print(po1.marks)
print(po2.name)
print(po2.marks)
print(person.mro())


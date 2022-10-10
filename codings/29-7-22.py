# print("hello")
# x={"name":"john","age":30}
# x["name"]="david"
# print(x)
# x["dob"]=2000
# print(x)
# x.update({"name":"sanjai"})
# print(x)
# y=x.get("name")
# print(y)
# z=x.keys()
# print(z)
# a=x.values()
# print(a)
# x.pop("name")
# print(x)
# x.popitem()
# print(x)
# x.clear()
# print(x)
#
#
# dic={"brand":"ford","color":"red","model":"g30"}
# b=dic.items()
# print(b)
# mydic=dic.copy()
# print(mydic)
#
#
# cars={"car1":{"name":"benz", "color":"red", "year":1998},
#       "car2":{"name":"audi", "color":"black", "year":1995},
#       "car3":{"name":"BMW", "color":"blue", "year":2000}}
# y=cars.keys()
# print(y)
# z=cars.values()
# print(z)
# cars.setdefault("car4","ferarri")
# print(cars)
# print(max(cars))
# print(min(cars))
# print(all(cars))
# print(any(cars))
#
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# result=dict(zip(keys,values))
# print(result)
#
#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["physics"])
#
#
#
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# result=dict.fromkeys(employees,defaults)
# print(result["Kelly"])
#
#
# x={"name":"loki",
#    "age":21,
#     "salary":25000,
#     "city":"new york"}
# print(x.keys())
#
#
# y={"name":"chris",
#    "age":24,
#    "salary":30000,
#    "city":"california"}
# k=["name","age"]
# for i in k:
#     y.pop(i)
#     print(y)
#
#
# z={"name":"sanjai","age":20}
# if 20 in z.values():
#         print("yes")
# else:
#     print("no")
#
#
#
# m={"maths":90,
#    "science":95,
#    "social":99,
#    "tamil":100,
#    "english":96}
# for i in m:
#     print(min(m,key=m.get))
#     break
#
#
#
# company={
#          "emp1":{"name":"john","age":25,"salary":25000},
#          "emp2":{"name":"peter","age":34,"salary":40000},
#          "emp3":{"name":"davis","age":28,"salary":30000}
# }
# company["emp3"]["salary"]=27000
# print(company)
#
#
#
# c={"name":"Sanjai",
#    "age":20,
#    "salary":20000,
#    "city":"chennai"
# }
# keys=["name","age"]
# for i in keys:
#     c.pop(i)
# print(c)
#
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dict4={}
# for j in (dic1,dic2,dic3):
#     dict4.update(j)
# print(dict4)
#
#
# n=int(input("enter the number"))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)
#
# m={"maths":90,
#    "science":95,
#    "social":99,
#    "tamil":100,
#    "english":96}
# print(sum(m.values()))
#
# x={"name":"loki",
#    "age":21,
#     "salary":25000,
#     "city":"new york"}
# print(sum(x.values()))
#
#
# def sum(n):
#     return n*n
# y=1,2,3,3,4
# z=list(map(sum,y))
# print(z)
#
# x={"name","age","year"}
# y={"sanjai",21,2000
# z=x.union(y)
# print(z)
#
# def sum(x):
#     return x
# print(sum(5
#           ))
#
# print('''ault'kelly''')

print(3/5*2)
print(8//3*3/2)
print(10%4)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("enter your choice")
print("1. addition")
print("2. subraction")
print("3. multiplication")
print("4. division")

while True:
    choice=input("enter the choice(1/2/3/4): ")

    if choice in ("1","2","3","4"):
        num1=float(input("enter the first number : "))
        num2=float(input("enter the second number : "))

        if choice == "1":
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == "2":
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice == "3":
            print(num1,"*",num2,"=",mul(num1,num2))
        elif choice == "4":
            print(num1,"/",num2,"=",div(num1,num2))


        nextcalculation=input("Do you want to continue(yes/no):")

        if nextcalculation == "no":
            print("thank you")
            break
        elif nextcalculation == "yes":
            continue
        else:
            print("please enter valid input!")
            break


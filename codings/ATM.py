totalbalance=100000
while True:
    print("\t$$$$ WELCOME TO SMART ATM $$$$\n")

    pin=0000
    s=int(input(" Please enter your ATM pin "))
    if s==pin:
        pass
    else:
        print(" please enter valid pin!\n")
        continue

    while True:

        print("1.check balance")
        print("2.withdraw money")
        print("3.deposit money")

        #totalbalance=100000
        n=input("enter the option ")
        if n =="1":
            print("TOTAL BALANCE IN YOUR ACCOUNT\n",totalbalance)
        elif n=="2":
            x=int(input("enter the amount to withdraw "))
            if x>20001:
                print("please enter amount less than 20000 !!! \n ")
                break

            print("successfully withdrawed")
            totalbalance=totalbalance-x


            print("REMAINING AMOUNT\n",totalbalance)
            print("\n")
            #continue
        elif n=="3":
            a=int(input("enter the amount to deposit "))
            totalbalance=totalbalance+a
            print("successfully deposited ")
            print("TOTAL AMOUNT\n",totalbalance)
        else:
            print("please enter valid input")

        h=input("do you want to continue transcation (yes/no) ")

        if h =="no":
            print("\t***THANK YOU FOR USING ATM***\n")
            break

        elif h =="yes":
            continue
        else:
            print("enter valid data!\n")
            break





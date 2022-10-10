#1	Write a Python program which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.
x=input("enter the number in seperated comma")
list=x.split(",")
tuple=tuple(list)
print("list=",list)
print("tuple=",tuple)

#2 Write a Python program to find whether a given number (accept from the user)
# is even or odd, print out an appropriate message to the user.
a=int(input("enter the number"))
if a%2==0:
    print("entered number is even")
else:
    print("entered number is odd")

#3 Write a Python program to test whether a passed letter is a vowel or not.

x=input("enter the letters")
if x in ("a","e","i","o","u"):
    print("yes,entered letter is vowel")
else:
    print("no,entered lettered letter is not a vowel")
#4 Write a Python program to print the following string in a specific format.

#               Twinkle, twinkle, little star,
#                   How I wonder what you are!
#                           Up above the world so high,
#                           Like a diamond in the sky.
#               Twinkle, twinkle, little star,
#                    How I wonder what you are

print("Twinkle,twinkle,little star,\n\t How I wonder what you are!\n\t\tUp above the world so high,\
      \n\t\tLike a diamond in the sky.\nTwinkle,twinkle, little star,\n\tHow I wonder what you are ")

#5	Write a Python program to get the Python version you are using
import sys
print("python version",sys.version)


#6  Write a Python program to display the current date and time
import datetime
c=datetime.datetime.now()
print(c)
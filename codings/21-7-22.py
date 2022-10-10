a="sanjai"
print(a[::-1])



x="amazon"
for n in x:
    if n in "abc":
        print("2",end="")
    elif n in "def":
        print("3",end="")
    elif n in "ghi":
        print("4",end="")
    elif n in "jkl":
        print("5",end="")
    elif n in "mno":
        print("6",end="")
    elif n in "pqrs":
        print("7",end="")
    elif n in "tuv":
        print("8",end="")
    elif n in "wxyz":
        print("9",end="")
    else:
        print("enter in alphabetics")


def largest(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
largest(2,4,5)


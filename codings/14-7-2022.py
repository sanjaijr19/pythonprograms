print("hello")

x=[1,3,4,7]
print("the sum is ",sum(x))
y=1
for i in x:
    y=y*i
print((y))

a=[]
if a:
    print("list is full")
else:
    print("list is empty")

k=("sanjaikumar","python","java.com")
j=k.count("a")
print(j)
print(len(k))
for i in k:
    print(len(i))

def counts(words):
    x=0
    for i in words:
        if i>1 and i[0]==[-1]:
            x+=1
        return x
    print(counts(["sas","lol","pip","kit"]))

    def match_words(words):
        ctr = 0

        for word in words:
            if len(word) > 1 and word[0] == word[-1]:
                ctr += 1
        return ctr

    print(match_words(['abc', 'xyz', 'aba', '1221']))


# Problem set 1
# A - Short questions: F,F,T,T,F,T
# A - Code analysis
listA = [1,2,3,4,5,6]
listB = [7,6,5,4,3,2]
listC = ["Apple", "Sauce", "Pizza"]

listA.append("Lucy")
listA.pop(0)
print(listA[2])
listB.append(listC.pop())
listC.append(listB[listA[4]])
print(listA.pop())

# B - Short questions: F, F, T, F
# B - Code analysis
myList = [1,2,3,4,5]
myOtherList = list()

for i in range(len(myList)):
    myOtherList.append(myList[i])

print(myOtherList)

# Programming questions
# Problem 1
    # sum all numbers 0-100; sum only even, sum only odd
n=0
for i in range(101):
    n = n + i

print(n)

e=0
i=0
while i <= 100:
    e = e + i
    i = i + 2

print(e)

o=0
i=1
while i <= 99:
    o = o + i
    i = i + 2

print(o)


# Problem 2
    # calculate average & sd of list
import math
nums = [55,60,75,43,10,75,23]

def avg(x):
    mean=sum(x)/len(x)
    diff = []
    for i in x:
        b=(i-mean)**2
        diff.append(b)
    ss = sum(diff)/(len(x)-1)
    sd = math.sqrt(ss)

    print(mean)
    print(sd)

avg(nums)

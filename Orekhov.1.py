def slicer(tup, num):
    if num in tup:
        x = tup.count(num)
        y = tup.index(num)
        print("(", end="")
        while tup:
            print(tup[y], end="")
            y += 1
            if y == len(tup):
                print(")")
                break
            print(", ", end="")
            if tup[y] == num:
                print(tup[y], end=") \n")
                break
    if num not in tup:
        print("()")

slicer((1,2,3),8)
slicer((1,8,3,4,8,8,9,2),8)
slicer((1,2,8,5,1,2,9),8)

# __________________________________________________________________________________________________
import random

def tuple_random(a,b):
    tup=tuple([random.randint(a,b) for i in range(10)])
    return tup

tup1=tuple_random(0,5)
tup2=tuple_random(-5,0)
print(tup1)
print(tup2)
tup3=tup1+tup2
print(tup3)
print("0 =", tup3.count(0))


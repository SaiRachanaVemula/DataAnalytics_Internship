#1.Python If-Else
#https://www.hackerrank.com/challenges/py-if-else/problem


i=int(input())
if i%2==0 and 2<i<5:
    print("Not Weird")
elif i%2==0 and 6<i<20:
    print("Weird")
elif i%2==0 and i>20:
    print("Not Weird")
else:
    print("Weird")

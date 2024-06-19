# 3 Write a python program that calculates the factorial of a given number.

n= int(input("enter the number"))

factorial=1
a=1
while a<=n:
    factorial=factorial*a
    a=a+1

    print(factorial)
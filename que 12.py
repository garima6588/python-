#Write a python program that calculates the sum of the digits of a given number.
n= int(input("enter the required number"))
a=0

while (n>0):
    a=a+n%10
    n=n//10
    print(a)

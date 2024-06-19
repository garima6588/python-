#Write a python program that generates the first n numbers in the Fibonacci sequence.
n= int(input("enter the number till you want to print fibonacci series"))
a=0
b=1
c=0
print(a)
print(b)

for i in range (1,n+1):
    c=a+b
    a=b
    b=c
    print(c)

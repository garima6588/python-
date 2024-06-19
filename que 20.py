#Write a python program that takes a list of numbers and returns their sum.

n=int(input("how many elements you want in the list"))
L=[]
for i in range(n):
    ele=int(input("enter the elements in the string"))
    L.append(ele)
    print(L)
s=0
for j in L:
    s+=j
    print(s)



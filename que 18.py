#Write a python program that checks if two strings are anagrams of each
#other.
def check(s1,s2):
    if sorted(s1)==sorted(s2):
        print("strings are in anagrams")
    else:
        print("strings are not in anagrams")

s1=str(input("enter the first string"))
s2=str(input("enter the second string"))
check(s1,s2)

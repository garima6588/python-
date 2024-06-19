#Write a program in python that counts the frequency of each character in a string

n= str(input("enter the word"))
freq = {}

for i in n:
    if i in freq:
        freq[i]=freq[i] + 1
    else:
        freq[i]=1
print("Count of all characters  is :\n "
      + str(freq))

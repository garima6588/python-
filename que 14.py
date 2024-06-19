#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints
# all the lines

a=(input("enter the line"))
while True:
    if a==(""):
        print("this cannot be printed")
        break

    else:
        print(a)
        break



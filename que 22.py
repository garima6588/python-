#Write a python program that returns the minimum and maximum values
#in a list of numbers.



a = [35, 41, 49, 37, 31,
     55, 23, 31, 18, 50,
     32, 37, 28, 27, 24, 35]

print("Min: ", pd.Series(a).idxmin())
print("Max: ", pd.Series(a).idxmax())
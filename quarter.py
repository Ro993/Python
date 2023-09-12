x = int(input("Enter a month (1-12): "))

if x >= 1 and x <= 3:
    print("Quarter 1")
elif x >= 4 and x <= 6:
    print("Quarter 2")
elif x >= 7 and x <= 9:
    print("Quarter 3")
elif x >= 10 and x <= 12:
    print("Quarter 4")
else:
    print("Please enter a number between 1 and 12")
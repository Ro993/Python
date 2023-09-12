
num = int(input("Enter a number (1-12): "))


if num == 1:
    month = "January"
elif num == 2:
    month = "February"
elif num == 3:
    month = "March"
elif num == 4:
    month = "April"
elif num == 5:
    month = "May"
elif num == 6:
    month = "June"
elif num == 7:
    month = "July"
elif num == 8:
    month = "August"
elif num == 9:
    month = "September"
elif num == 10:
    month = "October"
elif num == 11:
    month = "November"
elif num == 12:
    month = "December"
else:
    month = "Invalid input"

print(f"The month for {num} is {month}")

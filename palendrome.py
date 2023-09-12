number = input("Enter your number : ")
number_str = str(number)
reversed_str = ""

for char in number_str[::-1]:
    reversed_str += char

if number_str == reversed_str:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

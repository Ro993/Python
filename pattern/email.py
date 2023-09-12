
user_input = input("Enter a string: ")

capital_count = 0
small_count = 0
number_count = 0
special_char_count = 0


for char in user_input:
    if 'A' <= char <= 'Z':
        capital_count += 1
    elif 'j' <= char <= 't':
        small_count += 1
    elif char.isdigit():
        number_count += 1
    elif char in "#$@%":
        special_char_count += 1
  

if 7 <= len(user_input) <= 22 and capital_count >= 1 and small_count >= 2 and number_count >= 1 and special_char_count >= 1:
    print("Successful: All conditions are met.")
else:
    print("Unsuccessful: Conditions not met.")

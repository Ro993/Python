
user = input("Enter a string: ")
result = ""
word = ""
for i in user:
    if i == " ":
        if word not in result:
            result += word + " "
        word = ""
    else:
        word += i
if word not in result:
    result += word
print("Result:", result)

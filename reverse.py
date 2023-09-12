# a = input("Enter your string")
# rev = ""
# for char in a[::-1]:
#     rev += char
# print(rev)

########################################################
# def reverse(s):
# 	if len(s) == 0:
# 		return s
# 	else:
# 		return reverse(s[1:]) + s[0]    # using recursion
# s = "Hello Tiger"

# print("The reversed string : ", end="")
# print(reverse(s))

########################################################

a = "Hello, World!"
rev = ""
i = len(a) - 1

while i >= 0:
    rev += a[i]
    i=i-1

print(rev)
#########################################################




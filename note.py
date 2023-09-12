
x= int(input("Enter an amount (up to 50) ="))

fifty = 0
twenty = 0
ten = 0
five = 0
one= 0


if x >= 50:
    fifty = x // 50
    x %= 50

if x >= 20:
    twenty = x // 20
    x %= 20

if x >= 10:
    ten = x // 10
    x %= 10

if x >= 5:
    five = x // 5
    x %= 5

if x >= 1:
    one= x

print(f"Number of 50 notes: {fifty}")
print(f"Number of 20 notes: {twenty}")
print(f"Number of 10 notes: {ten}")
print(f"Number of 5 notes: {five}")
print(f"Number of 1 notes: {one}")


count = 65  

for i in range(1, 5):
    for j in range(1, i + 1):
        print(chr(count), end="")
        count += 1
    print("")

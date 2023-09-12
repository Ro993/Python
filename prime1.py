for x in range(201):
    flag = 1

    if x <= 1:
        flag = 0
    else:
        for i in range(2, x):
            if x % i == 0:
                flag = 0
                break

    if flag:
        print(f"{x} is prime")
    else:
        print(f"{x} is not prime")

            
        
            


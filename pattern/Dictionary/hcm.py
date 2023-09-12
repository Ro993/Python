def hcf_number(num1, num2):
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    
    # hcf = 1
    # i = 1

    while (True):
        if smaller % num1 == 0 and smaller % num2 == 0:
            print("hcf is ",smaller)
            break
        else:
            smaller+=1
hcf_number(10,20)            
       



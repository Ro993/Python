def lcmnumber(num1,num2):
    if(num1>num2):
        great=num1
    else:
        great=num2 
    print(great)  
         
    while(True):
        if(great %num1==0 and great %num2==0):
            print("lcm is ",great)
            break
        else:
           great+=1  
lcmnumber(2,7)    
    
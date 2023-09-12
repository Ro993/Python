num =153
sum=0
temp=num
while num>0:
    rem =num%10
    sum =sum+rem*rem*rem
    num=num//10
if(temp==sum):
    print("number is armstrong")
else:
    print("number is not armstrong")        
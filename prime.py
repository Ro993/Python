# numbers = [2,3,4,5,6,7,8,9,10,13,15]
# prime_numbers =[num for num in numbers if num>1 and all(num%i !=0 for i in range(2,num) )] 
# print(prime_numbers) 


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15]
prime_numbers = []

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print(prime_numbers)

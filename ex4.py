number = input("Input a number: ")
number = int(number)


if number > 1:
    for n in range(2,number):
        if (number % n) == 0:
            flag = True
            break
if flag:
    print(f'{number} is not a prime number')
else:
    print(f'{number} is a prime number')
    






            

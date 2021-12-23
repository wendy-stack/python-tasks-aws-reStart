numbers = list(range(1,51))
for n in numbers:
    if n % 3 == 0 and n % 5 == 0:
        print('Fizzbuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

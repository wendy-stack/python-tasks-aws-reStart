int = list(range(1,51))
print(int)
for number in int:
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    if number % 15 == 0:
        print("FizzBuzz")
    else:
        print(number)
    

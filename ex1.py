numbers = list(range(1500, 2700))

for number in numbers:
    if number % 7 == 0 and number % 5 == 0:
        print(number)

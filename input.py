'''message = input("Tell me something and i will echo it back to you: ")
print(message)'''

'''prompt = "If you tell me your name, I can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("Hello " + name.title() + "!")'''

'''age = input("How old are you? ")
age = int(age)
print("My age is " + str(age))'''

# a program that determines if you are tall enough to ride a rollercoaster

'''height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("You are tall enough to ride")
else:
    print("You are not eligible to ride")'''



'''number = input("Enter a number and i will tell you whether it is Odd or Even: ")
number = int(number)

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")'''

# a program that tells you what kind of car u would like 7-1
'''rental_car = input("What kind of car would you like? ")
print("Let me see if i can find you a " + rental_car)'''

# exercise 7-2
'''dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group >=8:
    print("Sorry we are out of tables, kindly wait or try again")
else:
    print("Your table is ready!")'''

# exercise 7-3

ask_number = input("Type a random number: ")
ask_number = int(ask_number)

if ask_number % 10 == 0:
    print("Your number is a multiple of 10")
else:
    print("Your number is not a multiple of 10")

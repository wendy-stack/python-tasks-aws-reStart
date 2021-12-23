import random

guess_number = int(input("Guess a random number between 1 to 9: "))
random_number = random.randint(1,9)
guess_attempt = 9

while guess_number != random_number:
    print("Try again")
    guess_attempt-=1
    print(f"Your guess attempt is remaining {guess_attempt}")
    guess_number = int(input("Guess a random number between 1 to 9: "))
    
print("Well guessed!")  

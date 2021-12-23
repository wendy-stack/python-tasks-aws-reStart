'''current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1'''

'''prompt = "\nTell me something and i will echo it back to you: "
prompt += "\nEnter 'quit' to end the program. "
#message = ""

while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)'''

'''active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)'''


 
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' to end the program. "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("You have been to " + city.title() + "!.")
    
    

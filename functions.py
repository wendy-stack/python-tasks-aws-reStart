'''def greet_user():
    print("Hello!") '''

'''def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('wendy')'''

'''def display_message():
    print("I learnt about Functions in this chapter!")

display_message()'''

'''def favorite_book(name):
    print("My favorite book is " + name.title())

favorite_book('Alice in Wonderland')'''
    
'''def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type.title())
    print("My " + animal_type.title() + "'s name is " + pet_name.title())
describe_pet('dog', 'charmy')'''

'''def make_shirt(size, message):
    print("Your shirt size is " + size.title() + " and your message is " +
          message.title() + "!.")
make_shirt('m','Amina FC')'''

'''def make_shirt(size = 'l', message = 'I love python'):
    print("Your size is " + size.title() + ", the message is " + message)
make_shirt('s')'''

'''def describe_city(city,country='poland'):
    print(city.title() + " is in " + country.title())
describe_city('Adelaide','Austrailia')'''

'''def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' '  + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('mary j','asken','blidge')
print(musician)'''
# a function running a list or dictionary
'''def build_person(first_name, last_name, age=''):
#Return a dictionary info about a person
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('katy','perry', '27')
print(musician)'''

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    break
    



'''pet_1 = {'name':'bonnie', 'type':'cat'}
pet_2 = {'name':'colore', 'type':'dog'}

pets = [pet_1, pet_2]
for pet in pets[0:2]:
    print(pet)'''

favorite_places = {
    'wendy':['london','lagos','mexico'],
    'ade':['texas','lagos','paris'],
    'taiwo':['lagos']
    }
for name, place in favorite_places.items():
    print(name.title() + "'s favorite places are " )
    for place in place:
        print(place.title())

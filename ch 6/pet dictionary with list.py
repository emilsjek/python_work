pet_0 = {
    'type':'dog',
    'owners_name':'jack',
}

pet_1 = {
    'type':'cat',
    'owners_name':'james',
}

pet_2 = {
    'type':'fish',
    'owners_name':'john',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    type = pet['type']
    owner = pet['owners_name'].title()
    print(f"The pet is a {type} and it's owner is {owner}.")
person_0 = {
    'first_name':'Kerry',
    'last_name':'Agabi',
    'age':'24',
    'city':'Carlow',
}

person_1 = {
    'first_name':'Oskar',
    'last_name':'Sadowski',
    'age':'21',
    'city':'Ashbourne',
}

person_2 = {
    'first_name':'Pauls',
    'last_name':'Dambergs',
    'age':'20',
    'city':'Talsi',
}

people = [person_0,person_1,person_2]



for person in people:
    fname = person['first_name'].upper()
    lname = person['last_name'].upper()
    age = person['age']
    city = person['city'].upper()
    print(f"{fname} {lname} is {age} and is from {city}")
    print()
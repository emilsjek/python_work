favourite_places = {
    'kerry': 'seattle',
    'ella':['madera','carlow','greece','costa rica'],
    'emils':'madeira'
}

for name, place in favourite_places.items():
    if type(place) is list:
        print(f"{name.title()}'s favourite places are:")
        for places in place:
            print(f"\t{places.title()}")
    else:
        print(f"{name.title()}'s favourite place is {place.title()}.")
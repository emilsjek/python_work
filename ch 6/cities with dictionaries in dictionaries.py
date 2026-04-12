cities = {
    'dublin':{
        'population':1000000,
        'county':'meath',
    },
    'carlow':{
        'population':30000,
        'county':'kildare',
    },
    'cork':{
        'population':300000,
        'county':'kerry',
    },
}

for keys, values in cities.items():
    population = values['population']
    county = values['county'].title()
    print(f"{keys.title()} is located in Co.{county} and has a population of: {int(population)}.")
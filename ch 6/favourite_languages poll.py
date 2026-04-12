favourite_languages = {
    'jen': 'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

friends = ['jen', 'sarah', 'edward', 'phil', 'kerry', 'josh']

for name in friends:
    if name in favourite_languages.keys():
        print(f"Thanks {name} for taking the poll.")
    else:
        print(f"Hey {name}, please take the poll!")
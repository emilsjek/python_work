def get_formatted_name(first, last, middle=''):
    """Make someones full name a variable"""
    if middle:
        full_name = f"{first} { middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

musician = get_formatted_name('ella',last='hendricken')
print(musician)
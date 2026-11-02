def build_profile(first, last, **user_info):
    """build a dictionary containing everything we know about a user"""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('Emils', 'Jekabsons', location='Carlow', job='PM', 
                             hobby='Powerlifting')
print(user_profile)
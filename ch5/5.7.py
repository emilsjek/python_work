users = ['admin', 'ella', 'emils', 'mark', 'oskar']

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()}. Would you like a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging on!")
else:
    print('We need more users!')
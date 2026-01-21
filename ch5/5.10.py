current_users = ['ella','josh','kerry','oskar','mark']

new_users = ['sean','cian','mark','ben','ben']

for user in new_users:
    if user in current_users:
        print('Username already taken, pick a different one')
    else:
        current_users.append(user)
        print('user name available') 
print(current_users)

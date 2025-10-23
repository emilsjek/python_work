guest_list = ['Jordan','Einstein','Jebb']

print(f'I would like to invite you to my party my \
dear friend {guest_list[0].title()}.')
print(f'I would like to invite you to my party my \
dear friend {guest_list[1].title()}.')
print(f'I would like to invite you to my party my \
dear friend {guest_list[-1].title()}.')

cant_make_it = guest_list.pop(-1)
print(f'Sorry everyone, {cant_make_it} wont be able to attend.')

new_guest = 'Childish Gambino'
guest_list.append(new_guest)

print(f'I would like to invite you to my party my \
dear friend {guest_list[0].title()}.')
print(f'I would like to invite you to my party my \
dear friend {guest_list[1].title()}.')
print(f'I would like to invite you to my party my \
dear friend {guest_list[-1].title()}.')

print('We got a bigger  table!')

guest_list.insert(0, 'Jojo Siwa')
guest_list.insert(2, 'Ella')
guest_list.append('Kim K')

for name in guest_list:
    print(f'I would like to invite you to my party my \
dear friend {name.title()}.')

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest.title()}, there's no room at the table!")

for left in guest_list:
    print(f"{left.title()}, you still have a seat at the table!")

while len(guest_list) > 0:
    del guest_list[0]

print(guest_list)
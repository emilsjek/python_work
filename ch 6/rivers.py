rivers = {
    'nile':'egypt',
    'shannon':'ireland',
    'colorado':'usa',
}
for river,country in rivers.items():
    print(f"The river {river}, runs through {country}.")

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)
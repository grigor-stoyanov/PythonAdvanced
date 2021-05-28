n = int(input())
vip = set()
regular = set()
guests = set()
for i in range(n):
    line = input()
    if line[0].isdigit():
        vip.add(line)
    else:
        regular.add(line)
while True:
    guest = input()
    if guest == 'END':
        break
    guests.add(guest)
print(f'{len((vip|regular)-guests)}')
for guest in sorted(tuple(vip-guests)):
    print(guest)
for guest in sorted(tuple(regular-guests)):
    print(guest)
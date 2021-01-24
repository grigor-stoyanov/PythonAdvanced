n = int(input())
parking = set()
for i in range(n):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        parking.add(car_number)
    elif direction == 'OUT':
        parking.remove(car_number)
if parking:
    print('\n'.join(parking))
else:
    print('Parking Lot is Empty')
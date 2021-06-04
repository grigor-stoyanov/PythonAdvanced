names = input().split(', ')
cmd = input()
heroes_dic = {name: {} for name in names}
while not cmd == 'End':
    hero, item, value = cmd.split('-')
    value = int(value)
    heroes_dic[hero][item] = heroes_dic[hero].get(item, value)
    cmd = input()
for name, items in heroes_dic.items():
    print(f'{name} -> Items: {len(items.keys())}, Cost: {sum(items.values())}')

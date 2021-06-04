countries = input().split(', ')
capitals = input().split(', ')
capitals_dic = {pair[0]: pair[1] for pair in zip(countries, capitals)}
for key,value in capitals_dic.items():
    print(f'{key} -> {value}')

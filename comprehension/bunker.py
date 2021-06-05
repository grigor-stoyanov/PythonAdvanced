# receive all categories
cat = {category: [] for category in input().split(', ')}

# start receiving data on items
n = int(input())
for i in range(n):
    category, item, properties = input().split(' - ')
    quality, quantity = properties.split(';')
    quality = int(quality.split(':')[1])
    quantity = int(quantity.split(':')[1])
    items = {item: (quality, quantity)}
    cat[category].append(items)
sum_items = sum([list(ele.values())[0][0] for category, item in cat.items() for ele in item])
print(f'Count of items: {sum_items}')
avg_quality = (sum([list(ele.values())[0][1] for category, item in cat.items() for ele in item]) / len(cat))
print(f'Average quality: {avg_quality:0.2f}')
print(f"{key} -> {', '.join([key for ele in value for key in ele])}" for key, value in cat.items())

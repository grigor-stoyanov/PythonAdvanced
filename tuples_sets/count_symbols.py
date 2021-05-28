line = input()
#line = tuple(line)
#count_ch = {}
# for ch in line:
#     count_ch[ch] = count_ch.get(ch, 0) + 1
# count_ch = dict(sorted(count_ch.items(), key=lambda x: x[0]))
# for ch,count in count_ch.items():
#     print(f'{ch}: {count} time/s')
count_ch = set()
for ch in line:
    count_ch.add((ch,line.count(ch)))
count_ch = list(sorted(list(count_ch)))
for ele in count_ch:
    print(f'{ele[0]}: {ele[1]} time/s')
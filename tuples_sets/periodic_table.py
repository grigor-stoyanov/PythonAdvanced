n = int(input())
periodic_table = set()
for i in range(n):
   periodic_table.update(input().split())
print('\n'.join(periodic_table))
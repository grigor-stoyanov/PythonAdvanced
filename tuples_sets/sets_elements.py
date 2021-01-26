n, m = list(map(int, input().split()))
n_set = set()
m_set = set()
for i in range(m + n):
    if i < n:
        n_set.add(input())
    else:
        m_set.add(input())
print('\n'.join(n_set & m_set))

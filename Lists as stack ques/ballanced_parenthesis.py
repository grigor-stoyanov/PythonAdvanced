sequence = input()
PAR_DICT = {'[': ']', '{': '}', '(': ')'}
stack = []
isBalanced = True
for i in range(len(sequence)):
    if sequence[i] in PAR_DICT.keys():
        stack.append(i)
    elif not stack:
        isBalanced = False
        break
    elif sequence[i] in PAR_DICT.values():
        if sequence[i] == PAR_DICT[sequence[stack.pop()]]:
            continue
        else:
            isBalanced = False
            break
if isBalanced:
    print('YES')
else:
    print('NO')

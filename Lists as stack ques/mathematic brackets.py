# stack the ( bracket indexes until a ) bracket is found
# slice the expression with the last index and current one
expression = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
s = []
for i in range(len(expression)):
    ch = expression[i]
    if ch == '(':
        s.append(i)
    elif ch == ')':
        print(expression[s.pop():i+1:])

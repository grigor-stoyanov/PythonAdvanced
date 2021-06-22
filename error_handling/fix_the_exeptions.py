# fixed typeError by casting to int
numbers_list = list(map(int, input().split(", ")))
result = 0
# fixed typeerror by iterating trough elements
for number in numbers_list:
    # number = numbers_list[i + 1]

    # changed condition logic to fix proper results
    if number <= 5:
        result *= number
    elif number > 5:
        result /= number

print(result)

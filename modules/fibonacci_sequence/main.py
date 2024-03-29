from modules.fibonacci_sequence.helper import generate_sequence, find_number

while not (command := input()) == 'Stop':
    data = command.split()
    if data[0] == 'Create':
        fib_nums = generate_sequence(int(data[-1]))
        print(fib_nums)
    else:
        result = find_number(int(data[-1]), fib_nums)
        print(f'The number - {int(data[-1])} is '
              f'at index {result}' if isinstance(result, int) else result)

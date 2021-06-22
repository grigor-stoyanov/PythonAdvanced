text = input()
try:
    times = int(input())

except ValueError:
    print('Variable must be an integer!')
# else only works if try has passed
# without else here there is a possibility of Name error
else:
    print(text * times)

# comprehension is a short way to code a sequence
nums = [ele for ele in range(6)]
# comprehension must be used for simple operations to make it readable
# there are 4 types of comprehension list,dictionary,set and generator
# they require les memory, shorter syntax, easier data manipulation
# filtering numbers
x = [1, 2, 3, 4, 5]
filtered = [each for each in x if each % 2 == 0]
# hard to debug
filtered2 = [True if each % 2 == 0 else False for each in x]
info = [('Peter', 22), ('Amy', 18), ('George', 35)]
dic = {key: value for key, value in info}
dic = {ele: ele ** 3 for ele in x}
# set has the same syntax as a dictionary except for the key-value pairs
unique = {ele for ele in nums}
matrix = [[j for j in range(3)] for i in range(4)]

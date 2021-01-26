import sys

# tuples are immutable list like objects but the objects inside can be mutable eg. tuple of lists
# however you can't assign values to elements of the tuple
my_tuple = (1, 2, 3)
tuple_of_lists = ([1, 2], [3], [4])
tuple_of_lists[2].append(5)
print(tuple_of_lists)
# much like strings you cant do my_tuple.append(5), my_tuple[2] = 5 but you can concatenate different tuples
# tuples with 1 element need to be declared with a comma not just mathematical brackets
my_tuple += (1,)
print(my_tuple)
print(sum(my_tuple))
print(max(my_tuple))
print(my_tuple)
my_tuple = tuple(map(lambda x: x + 1, my_tuple))
print(tuple(map(lambda x: x + 1, my_tuple)))
# tuples are used when we know that the data we are using is immutable
grade_book = {
    'Pesho': 5.6,
    'Gosho': 5.4
}
for (name, mark) in grade_book.items():
    print(sys.getsizeof(name, mark))
# works faster than a list because a list takes more space in memory
for [name, mark] in grade_book.items():
    print(sys.getsizeof([name, mark]))
# they have 2 methods count and index returning count and first index of an element in the tuple
# index can also find the first index of an element after a certain index
print(my_tuple.index(2, 0))
# to find all indexes of an element you need to cycle trough the elements of the tuple
indices = []
index = 0
while True:
    # try helps prevent the error of accessing an index which doesn't exist in the tuple
    try:
        new_index = my_tuple.index(2, index)
        indices.append(new_index)
        index = new_index + 1
    except ValueError:
        break
print(indices)
# tuples allow unpacking elements of the tuple in different variables
a, *b = my_tuple
print(a, b)
# set is an unordered non-linear mutable collection of unique elements
# they have mathematical set operations union,intersection,symmetric difference and others
my_set = set([1, 1, 3, 4, 5, 6, 7])
my_set.add(8)
my_set.remove(4)
print(my_set)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# all operators have their apropriate functions
print(f'union{a | b} intersection{a & b} subset {a < b} difference {a - b} sym diff{a ^ b}')


# like the dictionary its a hash table
# checking the elements of the set is constant regardless of numbers of elements in it
# hash is an integer given to a value string,integer float
# a set calculates this unique hash and enters it into a list
class CustomSet:
    resize_factor = 0.7

    def __init__(self, ):
        # creates a list with a certain capacity
        self.capacity = 8
        self.count = 0
        self.values = [None] * self.capacity

    def execute_resize_check(self):
        return self.capacity * self.resize_factor >= self.count

    # resizes to 70% of the list capacity when list exceeds its capacity

    def resize(self):
        old_values = self.values
        self.count = 0
        self.capacity *= 2
        self.values = [None] * self.capacity
        for nested_list in old_values:
            if nested_list:
                for value in nested_list:
                    self.add(value)

    def get_index(self, value):
        value_hash = hash(value)
        # we get an index range from 0 to +-capacity
        index = abs(value_hash) % self.capacity
        return index

    def add(self, value):
        index = self.get_index(value)
        if not self.values[index]:
            self.values[index] = []
        if value not in self.values[index]:
            self.values[index].append(value)
            self.count += 1
        if self.execute_resize_check():
            self.resize()

    def remove(self, value):
        index = self.get_index(value)
        if self.value[index]:
            return
        if value not in self.value[index]:
            return
        self.value[index].remove(value)
        self.count -= 1

    def contains(self, value):
        index = self.get_index()
        if  self.values[index]:
            return False
        if value not in self.values[index]:
            return False
        return True

    def __contains__(self, item):
        return self.contains(item)
    def __len__(self):
        return self.count
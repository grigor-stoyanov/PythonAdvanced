# stacks and queues are represented with lists in python with limited functionality
# last in last out structure example: deck of cards
# we can add and remove elements at specific space and can only see 1 element
class Stack:
    def __init__(self):
        self.internal_stack = []

    def push(self, value):
        self.internal_stack.append(value)

    def pop(self):
        return self.internal_stack.pop()

    def peek(self):
        return self.internal_stack[-1]

    def length(self):
        return self.internal_stack.len()


# Que is first in first out structure
# Que in a list is a lot slower since it requires rearranging of elements
class Que:
    def __init__(self):
        self.internal_que = []

    def enqueue(self, value):
        self.internal_que.append(value)

    def dequeue(self):
        self.internal_que.pop(0)

    def peek(self):
        return self.internal_que[0]

    def length(self):
        return len(self.internal_que)


# to increase speed we can use deque, append and popleft
# deque is a double linked list
from collections import deque

que = deque(["Eric", "John", "Michael"])
que.append('Toby')
que.popleft()
print(que)

# heap is a collection like the stack where the lowst element is always on top
from heapq import heapify, heappush, heappop

heap = [1, -5, 3, 2, 6, 4]
heapify(heap)
heappush(heap, -1)
heappop(heap)
print(heap)

# Speed and algorithm's of searching is determined with big O notations
# for example a list has On to find a specific element in it (it has to check for n elements)
# stacks and ques have a speed of O1 because they always present the first or last element

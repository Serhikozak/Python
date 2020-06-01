class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """

        :type item: list
        """
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    # def peek(self):
    #     return self.items[len(self.items)-1]


stack = Stack()
stack.push(4)
stack.push('Hypocricy')
stack.push(29)
stack.push(45)
# print(stack.peek())
print(stack.pop())
print(stack.size())
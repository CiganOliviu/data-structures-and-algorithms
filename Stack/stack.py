class Stack():

    def __init__(self):
        super(Stack, self).__init__()
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __is_empty(self):
        return self.items == []

    def peek(self):
        if not self.__is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

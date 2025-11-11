class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        if self.top:
            self.top.next = new
            new.prev = self.top
        self.top = new

    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.prev
        if self.top:
            self.top.next = None
        return data


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.pop())

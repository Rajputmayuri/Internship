class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new = Node(data)
        if not self.rear:
            self.front = self.rear = new
        else:
            self.rear.next = new
            new.prev = self.rear
            self.rear = new

    def dequeue(self):
        if not self.front:
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        return data


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.dequeue())

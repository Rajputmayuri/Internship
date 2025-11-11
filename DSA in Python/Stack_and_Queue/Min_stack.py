class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if not self.items:
            self.items.append([val, val])
        else:
            mini = min(val, self.items[-1][1])
            self.items.append([val, mini])

    def pop(self) -> None:
        if self.items:
            self.items.pop()

    def top(self) -> int:
        if len(self.items) == 0:
            return 0
        return self.items[-1][0]

    def getMin(self) -> int:
        if len(self.items) == 0:
            return 0
        return self.items[-1][1]


obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())

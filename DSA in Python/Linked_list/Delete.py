class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def delete(self, val):
        temp = self.head
        if temp and temp.val == val:
            self.head = temp.next
            return

        prev = None
        found = False

        while temp is not None:
            if temp.val == val:
                found = True
                break
            prev = temp
            temp = temp.next

        if found:
            prev.next = temp.next
        else:
            print("Node not found")


sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()
sll.delete(20)
sll.display()

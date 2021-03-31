class Queue:
    def __init__(self):
        self.items = []

    def push(self, item: any):
        return self.items.append(item)

    def pop(self) -> any:
        return self.items.pop(0)

    def empty(self) -> bool:
        return len(self.items) == 0

class Stack(Queue):
    def pop(self) -> any:
        return self.items.pop()

class ListNode:
    def __init__(self, val: any, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(val)

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, item: any):
        if self.head is None:
            self.head = ListNode(item)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = ListNode(item)

    def __repr__(self):
        string = ''
        n = self.head
        while n is not None:
            string += str(n.val)
            if n.next is not None:
                string += ' -> '
            n = n.next
        return string

    @staticmethod
    def from_iter(it) -> 'LinkedList':
        l = LinkedList()
        for i in it:
            l.push(i)
        return l

if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        q.push(i)
    while not q.empty():
        print(q.pop())
    s = Stack()
    for i in range(10):
        s.push(i)
    while not s.empty():
        print(s.pop())
    l = LinkedList.from_iter([2, 5, 3, 1, 6])
    print(l)

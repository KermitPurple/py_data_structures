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

    def reverse(self):
        n = self.head
        prev = None
        while n:
            n.next, n, prev = prev, n.next, n
        self.head = prev

    def copy(self) -> 'LinkedList':
        n = self.head
        new_list = LinkedList()
        curr = None
        while n:
            new_node = ListNode(n.val)
            if new_list.head:
                curr.next = new_node
                curr = curr.next
            else:
                new_list.head = new_node
                curr = new_list.head
            n = n.next
        return new_list

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

class TreeNode:
    def __init__(self, val: any, left: 'TreeNode' = None, right: 'TreeNode' = None, parent: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def leftmost(self):
        if self.left is None:
            return self
        return self.left.leftmost()

    def rightmost(self):
        if self.right is None:
            return self
        return self.right.rightmost()

    def insert(self, val: any):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val, parent = self)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val, parent = self)
            else:
                self.right.insert(val)

    def remove(self, val: any):
        if val == self.val:
            self.delete()
        elif val < self.val and self.left is not None:
            self.left.remove(val)
        elif val > self.val and self.right is not None:
            self.right.remove(val)

    def delete(self):
        is_left_child = self.parent.left is self
        if self.left is None and self.right is None:
            if is_left_child:
                self.parent.left = None
            else:
                self.parent.right = None

    def print_LNR(self):
        if self.left:
            self.left.print_LNR()
        print(self.val, end=' ')
        if self.right:
            self.right.print_LNR()

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val: any):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.root.insert(val)

    def remove(self, val: any):
        self.root.remove(val)

    def print_file_system(self):
        self._print_file_system(self.root)

    def _print_file_system(self, root: TreeNode, depth: int = 0):
        if root is None:
            return
        print('│ ' * (depth - 1) + '├─' * (depth > 0) + str(root.val))
        depth += 1
        self._print_file_system(root.left, depth)
        self._print_file_system(root.right, depth)

    def print_LNR(self):
        if self.root is not None:
            self.root.print_LNR()
        print()

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
    l2 = l.copy()
    print(l2)
    l2.reverse()
    print(l)
    print(l2)
    tree = BinaryTree()
    for i in [5, 3, 7, 4, 6, 2, 8, 9, 10]:
        tree.insert(i)
    tree.print_file_system()
    tree.print_LNR()
    tree.remove(10)
    tree.print_file_system()
    tree.print_LNR()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked:
    def __init__(self):
        self.start = None

    def push_back(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        current = self.start
        while current.next:
            current = current.next
        current.next = new_node

    def push_front(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        new_node.next = self.start
        self.start = new_node

    def pop_back(self):
        if self.start is None:
            raise IndexError('Empty list. ')
        current = self.start
        while current.next.next:
            current = current.next
        current.next = None

    def pop_front(self):
        if self.start is None:
            raise IndexError('Empty List. ')
        current = self.start
        self.start = self.start.next
        current.next = None

    def search(self, data):
        if self.start is None:
            raise IndexError('Empty list.')
        current = self.start
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def insert(self, pos, data, ):
        if isinstance(data, list):
            for i in data:
                self.insert(pos, i)
            return

        new_node = Node(data)
        if pos == 0:
            new_node.next = self.start
            self.start = new_node
            return
        current = self.start
        index = 0
        while current:
            if index == pos - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            index += 1
        raise IndexError("Position out of range. ")


    def display(self):
        ls = []
        current = self.start
        while current:
            ls.append(current.data)
            current = current.next
        return ls


ob = Linked()
ob.push_back(3)
ob.push_back(10)
ob.push_back(100)
ob.push_front(0)
ob.push_front(12)
ob.insert(2, 9)
print(ob.search(100))
print(ob.display())

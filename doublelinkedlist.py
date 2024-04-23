class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLinked:
    def __init__(self):
        self.start = None

    def push_back(self,data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        current = self.start
        while current.next:
            current = current.next
        new_node.prev = current
        current.next = new_node

    def push_front(self,data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        new_node.next = self.start
        self.start.prev = new_node
        self.start = new_node

    def pop_back(self):
        if self.start is None:
            raise IndexError("Empty list. ")
        current = self.start
        while current.next.next:
            current = current.next
        current.next = None

    def pop_front(self):
        if self.start is None:
            raise IndexError("Empty list. ")
        current = self.start
        self.start = self.start.next
        current.next = None

    def insert(self,pos,data):
        if isinstance(data,list):
            for i in data:
                self.insert(pos,i)
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        current = self.start
        index = 0
        while current:
            if index == pos - 1:
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                return
            current = current.next
            index += 1

    def remove(self,data):
        if self.start is None:
            raise IndexError("Empty list. ")

        if self.start.data == data:
            self.start = self.start.next

        current = self.start
        while current:
            if current.data == data:
                current.next.prev = current.prev
                current.prev.next = current.next
                return
            current = current.next



    def display(self):
        ls = []
        current = self.start
        while current:
            ls.append(current.data)
            current = current.next
        return ls

ob = DLinked()
ob.push_back(1)
ob.push_back(2)
ob.push_back(3)
ob.push_back(4)
ob.push_back(5)
ob.push_front(0)
ob.insert(1,800)
ob.remove(0)
print(ob.display())

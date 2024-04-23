class DynamicArray:
    def __init__(self):
        self.count = 0
        self.size = 1
        self.array = [None] * self.size

    def resize(self, new_size):
        new_arr = self.make_array(new_size)
        for i in range(self.count):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.size = new_size

    def make_array(self, size):
        return [None] * size

    def empty(self):
        if self.count == 0:
            return 'Is empty! '

    def mysize(self):
        return self.count

    def push_back(self, value):
        if self.count == self.size:
            self.resize(2 * self.size)
        self.array[self.count] = value
        self.count += 1

    def pop_back(self):
        if self.count == 0:
            raise IndexError('Index Error! Attempting to pop from an empty array.')
        self.count -= 1

    def push_front(self, value):
        if self.count == self.size:
            self.resize(2 * self.size)
        for i in range(self.count, 0, -1):
            self.array[i] = self.array[i - 1]
        self.array[0] = value
        self.count += 1

    def pop_front(self):
        if self.count == 0:
            raise IndexError('Index Error! Deleting to pop from an empty array.')
        for i in range(1, self.count):
            self.array[i - 1] = self.array[i]
        self.count -= 1

    def insert(self, index, value):
        if self.count == self.size:
            self.resize(2 * self.size)
        if index <= self.count:
            for i in range(self.count, index, -1):
                self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.count += 1

    def remove(self, index):
        if index <= self.count:
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]
        self.count -= 1

    def shrink(self):
        if self.count <= self.size // 4 and self.size > 1:
            new_size = max(self.size // 2, 1)
            self.resize(new_size)

    def display(self):
        return self.array[:self.count]


ob1 = DynamicArray()
ob1.push_back(1)
ob1.push_back(2)
ob1.push_back(3)
ob1.push_back(4)
ob1.push_back(5)
ob1.push_back(7)
ob1.push_back(8)
ob1.push_front(0)
ob1.push_front(10)
ob1.pop_front()
print(ob1.mysize())
ob1.insert(2, 100)
ob1.insert(0, 900)
print(ob1.display())
ob1.remove(2)
print(ob1.mysize())
print(ob1.display())





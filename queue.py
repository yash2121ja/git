"""Queue Module"""
class queue():
    def __init__(self):
        self.data = []
        self.max_size = 10

    def push(self, value):
        if not self.is_full():
            self.data.append(value)
        else:
            print("queue full")

    def data_reverse(self):
        self.data.reverse()
        print(self.data)

    def pop(self):
        if self.is_empty() is False:
            return  self.data.pop(0)

        else:
            print("queue empty ")
            return None

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.data) == self.max_size:
            print(len(self.data))
            return True
        else:
            return False

    def display_queue(self):
        print(self.data)
        
obj = queue()
for i in range(10):
    obj.push(i)
obj.data_reverse()

obj.display_queue()

for i in range(5):
    obj.pop()

obj.display_queue()
obj.data_reverse()

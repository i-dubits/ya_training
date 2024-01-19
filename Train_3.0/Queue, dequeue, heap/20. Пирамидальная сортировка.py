class Heap():
    def __init__(self):
        self.arr = [None] * 100000
        self.pos_last = 0

    def insert(self, value):
        self.arr[self.pos_last] = value
        self.shift_up(self.pos_last)
        self.pos_last += 1

    def shift_up(self, pos):
        while pos > 0 and self.arr[(pos - 1) // 2] < self.arr[pos]:
            self.arr[(pos - 1) // 2], self.arr[pos] = self.arr[pos], self.arr[(pos - 1) // 2]
            pos = (pos - 1) // 2

    def extract(self):
        max_val = self.arr[0]
        self.arr[0] = self.arr[self.pos_last - 1]
        self.shift_down(0)
        return max_val

    def shift_down(self, pos):
        left = pos * 2 + 1
        right = pos * 2 + 2
        while left < self.pos_last - 1:
            pos_max = left if self.arr[left] > self.arr[right] else right
            if self.arr[pos_max] > self.arr[pos]:
                self.arr[pos_max], self.arr[pos] = self.arr[pos], self.arr[pos_max]
                pos = pos_max
                left = pos * 2 + 1
                right = pos * 2 + 2
            else:
                break

        self.pos_last -= 1

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))

if len(arr) == 1:
    print(*arr)
else:
    my_heap = Heap()
    for i in range(len(arr)):
        my_heap.insert(arr[i])
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = my_heap.extract()
    print(*arr)

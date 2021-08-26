import sys


class BinHeap:
    def __init__(self):
        self.heap = []

    def show_tree(self, pos=0, level=0):
        if pos < len(self.heap):
            l = self.Left(pos)
            r = self.Right(pos)
            self.show_tree(l, level + 1)
            print(' ' * 4 * level + '->', self.heap[pos])
            self.show_tree(r, level + 1)

    def Parent(self, i):
        return i // 2

    def Left(self, i):
        return 2 * i + 1

    def Right(self, i):
        return 2 * i + 2

    def BuildMaxHeap(self):
        n = len(self.heap)

        for i in range(n // 2, -1, -1):
            self.MaxHeapify(n, i)

    def MaxHeapify(self, n, i):
        largest = i
        l = self.Left(i)
        r = self.Right(i)
        if l < n and self.heap[l] > self.heap[i]:
            largest = l

        if r < n and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.MaxHeapify(n, largest)

    def BuildMinHeap(self):
        n = len(self.heap)
        for i in range(n // 2, -1, -1):
            self.MinHeapify(n, i)

    def MinHeapify(self, n, i):
        smallest = i
        l = self.Left(i)
        r = self.Right(i)
        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.MinHeapify(n, smallest)

    def HeapMaxSort(self):
        n = len(self.heap)
        self.BuildMaxHeap()
        for i in range(n - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]  # свап
            self.MaxHeapify(i, 0)

    def HeapMinSort(self):
        n = len(self.heap)
        self.BuildMinHeap()
        for i in range(n - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]  # свап
            self.MinHeapify(i, 0)

    # PART 2

    def HeapMax(self):
        return self.heap[0]

    def HeapExtractMax(self):
        if len(self.heap) < 1:
            raise Exception("Черга порожня")
        max = self.heap[0]
        self.heap.pop(0)
        size = len(self.heap)
        self.MaxHeapify(size, 0)
        return max

    def HeapIncreaseKey(self, i, key):
        if key < self.heap[i]:
            raise Exception("Новий ключ менше поточного")
        self.heap[i] = key
        while i >= 1 and self.heap[self.Parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.Parent(i)] = self.heap[self.Parent(i)], self.heap[i]
            i = self.Parent(i)

    def MaxHeapInsert(self, key):
        size = len(self.heap)
        self.heap.append(-sys.maxsize)
        self.HeapIncreaseKey(size, key)

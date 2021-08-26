from random import randint

class notRand:
    def cleanCounter(self):
        self.counter = 0
    counter = 0
    def partition(self,array, begin, end):
        pivot = begin
        for i in range(begin+1, end+1):
            if array[i] <= array[begin]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
        array[pivot], array[begin] = array[begin], array[pivot]
        return pivot

    def quick_sort(self,array, begin=0, end=None):
        self.counter += 1
        if end is None:
            end = len(array) - 1
        if begin >= end:
            return
        pivot = self.partition(array, begin, end)
        self.quick_sort(array, begin, pivot - 1)
        self.quick_sort(array, pivot + 1, end)

        return array


class rand:
    counter = 0
    def partition(self,array, begin, end):
        pivot = begin
        for i in range(begin+1, end+1):
            if array[i] <= array[begin]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
        array[pivot], array[begin] = array[begin], array[pivot]
        return pivot

    def RandomizedPartition(self,array,begin,end):
        i = randint(begin,end)
        array[end], array[i] = array[i], array[end]
        return self.partition(array,begin,end)

    def RandomizedQuickSort(self,array,begin = 0,end=None ):
        if end is None:
            end = len(array) - 1
        if begin< end:
            self.counter +=1
            q = self.RandomizedPartition(array, begin, end)
            self.RandomizedQuickSort(array, begin, q - 1)
            self.RandomizedQuickSort(array, q + 1, end)

        return array
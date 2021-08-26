class Hash:
    def __init__(self,maxsize):
        self.max = maxsize
        self.h = []
        for i in range(self.max):
            self.h.append([])

    def hash_function(self, key):
        i = key % self.max
        return i

    def ChainedHashInsert(self, key):
        index = self.hash_function(key)
        if key in self.h[index]:
            return -1
        else:
            self.h[index].append(key)
            return index

    def ChainedHashSearch(self, key):
        index = self.hash_function(key)
        bucket = self.h[index]
        for i,v in enumerate(bucket):
            if v == key:
                return i

    def ChainedHashDelete(self, key):
        index = self.hash_function(key)
        key_exists = False
        bucket = self.h[index]
        for i, k in enumerate(bucket):
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))

    def ChainedHashShow(self):

        for i in range(self.max):
            print(i, end=" ")
            for j in self.h[i]:
                print("-->", end=" ")
                print(j, end=" ")
            print()


    def HashInsert(self, key):
        i = 0
        while i < self.max:
            j = self.hash_function(key)
            if key not in self.h[j]:
                self.h[j].append(key)
                return j
            else:
                i += 1

    def HashSearch(self,key):
        i = 0
        j = self.hash_function(key)
        while self.h[j][i] != None and i <= self.max:
            if(self.h[j][i] == key):
                return i
            i += 1
        return -1

    def HashDelete(self,key):
        index = self.hash_function(key)
        element = self.HashSearch(key)
        self.h[index][element] = None

    def HashShow(self):
        for i in self.h:
            print(i, end="")

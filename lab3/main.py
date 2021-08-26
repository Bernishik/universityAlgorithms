import heap


def part1():
    # PART 1
    h = heap.BinHeap()
    h.heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    print("Max tree:")
    h.BuildMaxHeap()
    h.show_tree()
    print("Min tree:")
    h.BuildMinHeap()
    h.show_tree()
    print("Max sort arr:")
    h.HeapMaxSort()
    print(h.heap)
    print("Min sort arr:")
    h.HeapMinSort()
    print(h.heap)


def part2():
    # PART 2
    h = heap.BinHeap()
    h.heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    print(h.heap)
    max = h.HeapExtractMax() # Витягнути найбільший елемент
    print(h.heap)
    print("Max element: " + str(max))
    h.HeapIncreaseKey(8,15) # збільшує значення 8 елементу до 15
    print(h.heap)
    h.MaxHeapInsert(124) # вставити елемент 124 в купу
    print(h.heap)


# part1()
part2()

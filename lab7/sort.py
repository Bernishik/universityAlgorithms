def countSort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
    return arr



def RadixSort(arr, d):
    d = 10**d
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(d)]
        for  i in arr:
            tmp = i // placement
            buckets[tmp % d].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(d):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        placement *= d
    return arr
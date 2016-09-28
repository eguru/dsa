def insertionSort(arr):
    e = arr[-1]
    j = len(ar) - 2 # second last position
    while j >= 0 and arr[j] > e:
        arr[j+1] = arr[j]
        print " ".join([str(c) for c in arr])
        j -= 1
    arr[j+1] = e
    print " ".join([str(c) for c in arr])
    return ""

m = int(raw_input())
ar = [int(i) for i in raw_input().strip().split() if i.strip()]
insertionSort(ar)

def insertionSort(arr):
    o = []
    for i, e in enumerate(arr):
        j = i - 1
        while j >= 0 and arr[j] > e:
            arr[j+1] = arr[j]
            #print " ".join([str(c) for c in arr])
            j -= 1
        arr[j+1] = e
        p = " ".join([str(c) for c in arr])
        o.append(p)
    print "\n".join(o[1:])
    return ""

m = int(raw_input())
ar = [int(i) for i in raw_input().strip().split() if i.strip()]
insertionSort(ar)

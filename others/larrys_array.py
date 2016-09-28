import sys

#arr = [int(i.strip()) for i in "17 21 2 1 16 9 12 11 6 18 20 7 14 8 19 10 3 4 13 5 15".split() if i.strip()]
#arr = [int(i.strip()) for i in sys.argv[1:] if i.strip()]

def rotate(j, k, l, arr):
    a,b,c = arr[j:l+1]
    rotations = (
            (a,b,c), 
            (b,c,a), 
            (c,a,b)
    )
    for a,b,c in rotations:
        if a < c:
            arr[j] = a
            arr[k] = b
            arr[l] = c

    return arr

def inversions(i, arr):
    j = i+1
    inversion_count = 0
    while j < len(arr):
        if arr[i] >= arr[j]:
            inversion_count += 1
        j += 1
    return inversion_count

def larrys_array_sort(arr):
    inversed = [False]*len(arr)
    i = 0
    quit = False
    while not quit and i < len(arr):
        inversion_count = inversions(i, arr)
        #print i, arr[i], inversion_count
        while i < len(arr) and inversion_count == 0:
            inversed[i] = True
            i += 1
            if i >= len(arr):
                quit = True
                break
            inversion_count = inversions(i, arr)
            #print i, arr[i], inversion_count
        if i < len(arr) -2:
            j = i
            #print i, j, len(arr) - 2
            #sys.exit(-1)
            while j < len(arr) - 2:
                k = j+1
                l = j+2
                #print "Before rotate: ", i, j, k, l, arr
                arr = rotate(j, k, l, arr)
                #print "After rotate: ", i, j, k, l, arr
                j += 1
        else:
            quit = True
            break

    if all(inversed):
        print "YES"
    else:
        print "NO"

for t in range(int(raw_input().strip())):
    n = int(raw_input().strip())
    arr = [int(i.strip()) for i in raw_input().split() if i.strip()]
    larrys_array_sort(arr)


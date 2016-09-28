
def max_subarray(arr):

    s = 0
    e = len(arr)
    max_sum = 0
    max_sum_so_far = 0
    max_sum_positives = 0
    count_negatives = 0

    for i, val in enumerate(arr):
        if val >= 0:
            max_sum_positives += val
        else:
            count_negatives += 1

        max_sum += val
        if max_sum < 0:
           # reset
           max_sum = 0
        if max_sum_so_far < max_sum:
           max_sum_so_far = max_sum
    
    if count_negatives == len(arr):
        arr.sort()
        max_sum_so_far = arr[-1]
        max_sum_positives = max_sum_so_far
    
    print max_sum_so_far, max_sum_positives
 
for t in range(int(raw_input())):
    n = int(raw_input())
    arr = [ int(i.strip()) for i in raw_input().split() if i.strip() ]
    max_subarray(arr)
     

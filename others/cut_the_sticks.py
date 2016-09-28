

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

while len(arr) > 0:
    print len(arr)
    min_stick = min(arr)
    arr = [stick - min_stick for stick in arr if (stick-min_stick) > 0]

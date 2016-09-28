

arr = []
for t in range(int(raw_input())):
   arr.append(int(raw_input().strip()))

candies = [1]*len(arr)

for i  in range(0, len(arr)-1):
    if arr[i] < arr[i+1]: # higher rating means less number
        candies[i+1] += 1
    elif arr[i] > arr[i+1]:
        candies[i] += 1
print reduce(lambda x, y: x+y, candies)

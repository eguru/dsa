

n = int(raw_input().strip())
arr = [int(i.strip()) for i in raw_input().split() if i.strip()]

stack = []
top = None
area = -1
max_area = -1
i = 0

def remove(i, stack, arr, max_area):
    top = stack.pop()
    if not stack:
        area = arr[top] * i
    else:
        area = arr[top] * (i - stack[-1] -1)
    if max_area < area:
        max_area = area
    return max_area

while i < len(arr):
    if not stack or arr[i] >= arr[stack[-1]]:
        stack.append(i)
        i += 1
    else:
        max_area = remove(i, stack, arr, max_area)

while stack:
    max_area = remove(i, stack, arr, max_area)

print max_area        

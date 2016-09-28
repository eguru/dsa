
arr = []
stack_max = None
for t in range(int(raw_input())):
    q = [int(i.strip()) for i in raw_input().split() if i.strip()]
    if q[0] == 1:
        x = q[1]
        arr.insert(0, q[1])
        if x > stack_max:
            stack_max = x
    elif q[0] == 2:
        y = arr.pop(0)
        if arr:
            if y == stack_max:
                stack_max = max(arr)
        else:
            stack_max = None
    elif q[0] == 3:
        print stack_max

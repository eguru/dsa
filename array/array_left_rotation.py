

n, d = [i.strip() for i in raw_input().split() if i.strip()]
arr = [i.strip() for i in raw_input().split() if i.strip()]
print " ".join(arr[int(d):] + arr[:int(d)])

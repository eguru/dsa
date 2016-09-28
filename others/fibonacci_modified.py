
n, n1, n2 = [int(i.strip()) for i in raw_input().split() if i.strip() ]

n_val = 0

for i in range(2, n2):
    n_val = n1**2 + n
    print i, n, n1, n_val
    n = n1
    n1 = n_val

print n_val

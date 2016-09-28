


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    h = 1
    if n != 0:
        for i in range(1, n+1):
            if i % 2 == 0:
                h += 1
            else:
                h *= 2
    print h

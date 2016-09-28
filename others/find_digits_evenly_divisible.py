t = int(raw_input().strip())
for a0 in xrange(t):
    n = raw_input().strip()
    counter = 0  
    for c in n:
        c = int(c)
        if c > 0 and int(n) % c == 0:
            counter += 1
    print counter
    

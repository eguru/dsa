n = int(raw_input().strip())
l = [int(i.strip()) for i in raw_input().split() if i.strip()]
l.sort()
l.reverse()
x = l[0]
i = 1
while i < len(l) and x == l[i]:
    i += 1
print l[i]



d = { }
for i in range(int(raw_input())):
    toks = raw_input().split()
    d.setdefault(toks[0], map(float, toks[1:]))

marks = d[raw_input().strip()]
print "%.2f" % (reduce(lambda x,y: x+y, marks) / float(len(marks)))

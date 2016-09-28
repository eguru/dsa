
n = int(raw_input().strip())
l = []
for i in range(n):
    toks = [i.strip() for i in raw_input().split() if i.strip()]
    cmd = toks[0]
    vals = toks[1:]
    if cmd != "print":
        cmd += "("+",".join(vals)+")"
        eval("l."+cmd)
    else:
        print l


    
    

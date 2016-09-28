import string
n = int(raw_input().strip())
alpha = list(string.ascii_lowercase)[:n][::-1]
_a = []
_b = []
_d = []
p = (n*2)-1 # alphabets
p += (p - 1) # -
for a in alpha:
    _a.append(a)
    _c = "-".join(_a + list(reversed(_b)))
    _d.append(_c)
    print _c.center(p, "-")
    _b.append(a)
for a in reversed(_d[:-1]):
    print a.center(p, "-")
    

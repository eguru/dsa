
import string
letters = string.ascii_lowercase
d = { c.strip().lower(): 0 for c in raw_input().strip() if c.strip() }
k = d.keys()
k.sort()
if letters == "".join(k):
    print "pangram"
else:
    print "not pangram"

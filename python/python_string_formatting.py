n = int(raw_input().strip())
padding = len(bin(n)[2:])
for i in range(1, n+1):
    print str(i).rjust(padding), str(int(oct(i))).rjust(padding), hex(i)[2:].upper().rjust(padding), bin(i)[2:].rjust(padding)

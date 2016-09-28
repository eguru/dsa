

def xy1(x, y, lastSeq, sequences):
    seq_num = ( x ^ lastSeq ) % len (sequences)
    s = sequences[seq_num][:]
    s.append(y)
    sequences[seq_num] = s

def xy2(x, y, lastSeq, sequences):
    seq_num = ( x ^ lastSeq ) % len (sequences)
    s = sequences[seq_num]
    if s:
        si = y % len(s)
        lastSeq = s[si]
    return lastSeq

seq, queries = [int(i.strip()) for i in raw_input().split() if i.strip()]
lastSeq = 0
newLastSeq = 0
sequences = [[]]*seq

if seq >= 1 and seq <= 10**5 and queries >= 1 and queries <= 10**5:
    for q in range(queries):
        qtype, x, y = [int(i.strip()) for i in raw_input().split() if i.strip()]
        if x >= 0 and x <= 10**9 and y >= 0 and y <= 10**9:
            if qtype == 1:
                xy1(x, y, lastSeq, sequences)
            elif qtype == 2:
                newLastSeq = xy2(x, y, lastSeq, sequences)

            if newLastSeq != lastSeq:
                lastSeq = newLastSeq
                print newLastSeq
            #print x, y, lastSeq, newLastSeq, sequences

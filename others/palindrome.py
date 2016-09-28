def make_same2(s_list, i, j):
    total_moves = 0
    d = {}
    if i < j:
        smaller = i
        larger = j
        if s_list[i] > s_list[j]:
             smaller = j
             larger = i
        d_key = "{}_{}".format(s_list[larger], s_list[smaller])
        if d_key in d:
            smaller_val, tm = d[d_key]
            s_list[larger] = smaller_val
            total_moves += tm
        else:
            while s_list[larger] > s_list[smaller]:
                s_list[larger] = chr(ord(s_list[larger]) -1) 
                total_moves += 1
            d.setdefault(d_key, (s_list[smaller], total_moves))
            total_moves += make_same(s_list, i+1, j-1)
    return total_moves

def make_same(s_list):
    total_moves = 0
    d = {}
    i = 0
    j = len(s_list) - 1
    while i < j:
        smaller = i
        larger = j
        if s_list[i] > s_list[j]:
            smaller = j
            larger = i
        while s_list[larger] > s_list[smaller]:
            s_list[larger] = chr(ord(s_list[larger]) -1) 
            total_moves += 1
        i += 1
        j -= 1
    return total_moves


for t in range(int(raw_input())):
     s = raw_input().strip()
     s_list = list(s)
     reversed_s = s_list[:].reverse()
     if s == reversed_s:
         print 0
     else:
         #total_moves = make_same(s_list, 0, len(s) -1)
         total_moves = make_same(s_list)
         print total_moves
     
             
        


def findMinInsertions(s):
    
    i = 0
    j = len(s) - 1
    inserts_r2l = []
    while i < j:
        if s[i].lower() != s[j].lower():
            inserts_r2l.append((i, s[j]))
        else:
            i += 1
        j -= 1

    i = 0
    j = -1
    inserts_l2r = []
    while i < (len(s) -1):
        if s[i].lower() != s[j].lower():
            inserts_l2r.append((len(s) - j, s[i]))
        else:
            j -= 1
        i += 1

    minArr = inserts_r2l
    maxArr = inserts_l2r
    if minArr and maxArr and len(minArr) > len(maxArr):
        minArr = maxArr
    elif not minArr and maxArr:
        minArr = maxArr
   
    minArr.reverse()
    s_list = list(s)
    for index, val in minArr:
        s_list.insert(index, val)
    print "".join(s_list),
    return "total inserts : ", len(minArr)   

s = raw_input().strip()
total_moves = findMinInsertions(s)
print total_moves
     
             
        

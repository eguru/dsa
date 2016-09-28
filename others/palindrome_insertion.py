def is_palindrome(min_s, s):
    ms = "".join(min_s) + s
    reversed_s = list(ms)
    reversed_s.reverse()
    reversed_s = "".join(reversed_s)
    print ms.lower(), reversed_s.lower()
    return ms.lower() == reversed_s.lower()

def findMinInsertions(s):
    s = s.strip()
    total_insertion = 0
    i = 0
    j = len(s) - 1
    min_s = []
    while not is_palindrome(min_s, s):
        if s[i] != s[j]:
            min_s.insert(i, s[j])
            total_insertion += 1
        i += 1
        j -= 1
    return total_insertion

s = raw_input().strip()
total_moves = findMinInsertions(s)
print total_moves
     
             
        

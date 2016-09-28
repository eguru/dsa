
b = {
    "{" : "}",
    "[" : "]",
    "(" : ")",
}

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    s_stack = []
    
    for c in s:
        if c in ("{", "[", "("):
            s_stack.append(c)
            #print s_stack, ">>>>>>>>>" 
        else: # closing bracket
            if s_stack:
                open_bracket = s_stack[-1]
                #print s_stack, open_bracket, c, "<<<<<<<<<<<"
                if open_bracket in b and c == b[open_bracket]:
                   s_stack.pop()
                else:
                    s_stack.append(-1)
                    break
            else:
                s_stack.append(-1)
                break
    if len(s_stack) == 0: 
        print "YES"
    else:
        print "NO"

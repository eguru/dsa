
s = ""
operation_stack = []

def append(operation_stack, s, x):
    operation_stack.append(s)
    return s+x

def delete(operation_stack, s, x):
    operation_stack.append(s)
    return s[:-int(x)]

def pprint(operation_stack, s, x):
    print(s[int(x)-1])
    return s

def undo(operation_stack, s, x):
    s = operation_stack.pop()
    return s

operation_map = {
        "1" : append,
        "2" : delete,
        "3" : pprint,
        "4" : undo,
}

for t in range(int(raw_input().strip())):
    toks = [i.strip() for i in raw_input().split() if i.strip()]
    x = None
    if len(toks) == 2:
        operation, x = toks
    else:
        operation = toks[0]
    
    func = operation_map[operation]
    s = func(operation_stack, s, x)
    

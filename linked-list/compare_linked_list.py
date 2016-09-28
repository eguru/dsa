def CompareLists(headA, headB):
    if not headA and not headB:
        return 1
    elif not headA and headB:
        return 0
    elif headA and not headB:
        return 0
    currentA = headA
    currentB = headB
    while currentA and currentB:
        if currentA.data != currentB.data:
            return 0
        currentA = currentA.next
        currentB = currentB.next
    if not currentA and not currentB:
        return 1
    return 0



def MergeLists(self, headA, headB):
    if not headA and not headB:
        return headA
    elif not headA:
        return headB
    elif not headB:
        return headA
    else:
        currentA = headA
        currentB = headB
        head = currentA
        previousA = None
        if currentB.data < currentA.data:
            head = currentB
            currentA = headB
            currentB = headA

        while currentB:
            while currentA and currentB.data >= currentA.data:
                previousA = currentA
                currentA = currentA.next

            if previousA:
                # B data is greater
                nextB = currentB.next
                currentB.next = previousA.next
                previousA.next = currentB
                currentB = nextB
        return head


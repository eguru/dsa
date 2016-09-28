def Reverse(head):
    current = head
    previous = None
    while current:
        previous = current
        currentPrev = current.prev
        currentNext = current.next
        current.next = currentPrev
        current.prev = currentNext
        current = currentNext
        if current:
            current.prev = previous
    head = previous
    return head


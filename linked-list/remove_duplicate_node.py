def RemoveDuplicates(head):
    current = head
    while current and current.next:
        currentNext = current.next
        while currentNext and current.data >= currentNext.data:
            current.next = currentNext.next
            currentNext = None
            currentNext = current.next
        current = current.next
    return head


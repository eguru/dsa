def InsertNth(head, data, position):
    n = Node(data)
    if position == 0:
        n.next = head
        return n
    i = 0
    current = head
    while i < position-1 and current:
        i += 1
        current = current.next

    n.next = current.next
    current.next = n
    return head
        
        

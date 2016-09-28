def SortedInsert(head, data):
    if not head:
        n = Node(data)
        head = n
        return head
    n = Node(data)
    current = head
    previous = None
    while current and current.data < data:
        previous = current
        current = current.next

    if previous:
        n.next = current
        previous.next = n
        n.prev = previous
    else: # at head
        n.next = head
        head = n
    return head


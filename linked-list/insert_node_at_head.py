def Insert(head, data):
    n = Node(data)
    if head:
        n = Node(data)
        n.next = head
    return n

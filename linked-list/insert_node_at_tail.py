def Insert(head, data):
    if not head:
        n = Node(data)
        return n
    else:
        current = head
        while current and current.next:
            current = current.next
        if current:
            n = Node(data)
            current.next = n
        return head

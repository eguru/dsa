def GetNode(head, position):
    d = []
    current = head
    while current:
        d.append(current.data)
        current = current.next
    if d:
        return d[-(position+1)]


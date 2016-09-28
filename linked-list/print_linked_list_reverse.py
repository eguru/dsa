def ReversePrint(head):
    d = []
    current = head
    while current:
        d.append(str(current.data))
        current = current.next
    if d:
        print "\n".join(reversed(d))

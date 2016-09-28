def Reverse(self, head):
    nodes = []
    if head:
        current = head
        while current:
            nodes.append(current)
            current = current.next
        if nodes:
            for i in reversed(range(1, len(nodes))):
                n = nodes[i]
                n.next = nodes[i-1]
            nodes[0].next = None
            head = nodes[-1]
    return head

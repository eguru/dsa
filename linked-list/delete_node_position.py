def Delete(head, position):
    if position == 0:
        new_head = head.next
        head = new_head
    else:
        current = head
        i = 0
        while i < position-1 and current:
            i += 1
            current = current.next
        del_node = current.next
        current.next = current.next.next
        del_node.next = None
    return head

class Node(object):
    
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList(object):
    
    def __init__(self, data):
        self.head = Node(data)

    def addNode(self, data):
        n = Node(data)
        current = self.head
        while current and current.next:
            current = current.next
        current.next = n
        n.prev = current

    def SortedInsert(self, head, data):
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
     
    def Reverse(self, head):
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
        
    def pprint(self):
        
        d = ["NULL"]
        current = self.head
        while current:
            d.append(str(current.data))
            current = current.next
        d.append("NULL")
        print "<->".join(d)

def l1(n):
    l = DoubleLinkedList(1)
    for i in range(2, n+1):
        l.addNode(i)
    l.addNode(8)
    return l
def l2():
    l = DoubleLinkedList(1)
    return l

if __name__ == "__main__":
    l = l1(6)
    l.pprint()
    l.head = l.SortedInsert(l.head, 5)
    l.pprint()
    l.head = l.SortedInsert(l.head, 0)
    l.pprint()
    l.head = l.SortedInsert(l.head, 7)
    l.pprint()
    l.head = l.SortedInsert(l.head, 9)
    l.pprint()
    #l.head = l.SortedInsert(None, 9)
    #l.pprint()
    l.head = l.Reverse(l.head)
    l.pprint()
    l = l2()
    l.head = l.Reverse(l.head)
    l.pprint()

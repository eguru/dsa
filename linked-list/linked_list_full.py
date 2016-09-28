class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    
    def __init__(self, data):
        self.head = Node(data)
    
    def addNode(self, data):
        n = Node(data)
        current = self.head
        while current and current.next:
            current = current.next
        current.next = n

    def Reverse(self, head):
        nodes = []
        nodes_data = []
        if head:
            current = head
            while current:
                nodes.append(current)
                nodes_data.append(current.data)
                current = current.next
            if nodes:
                print nodes_data
                for i in reversed(range(1, len(nodes))):
                    n = nodes[i]
                    n.next = nodes[i-1]
                nodes[0].next = None
                self.head = nodes[-1]
    
    def CompareLists(self, headA, headB):
        if not headA and not headB:
            return 1
        elif not headA and headB:
            return 0
        elif headA and not headB:
            return 0
        currentA = headA
        currentB = headB
        while currentA and currentB:
            if currentA.data != currentB.data:
                return 0
            currentA = currentA.next
            currentB = currentB.next
        if not currentA and not currentB:
            return 1
        return 0

    def MergeLists(self, headA, headB):
        if not headA and not headB:
            return headA
        elif not headA:
            return headB
        elif not headB:
            return headA
        else:
            currentA = headA
            currentB = headB
            head = currentA
            previousA = None
            if currentB.data < currentA.data:
                head = currentB
                currentA = headB
                currentB = headA
                
            while currentB:
                while currentA and currentB.data >= currentA.data:
                    previousA = currentA
                    currentA = currentA.next
                
                if previousA:    
                    # B data is greater
                    nextB = currentB.next
                    currentB.next = previousA.next
                    previousA.next = currentB
                    currentB = nextB
            return head        
    
    def GetNode(self, head, position):
        d = []
        current = head
        while current:
            d.append(current.data)
            current = current.next
        if d:
            return d[-(position+1)]    

    def RemoveDuplicates(self, head):
        current = head
        while current and current.next:
            currentNext = current.next
            while currentNext and current.data >= currentNext.data:
                current.next = currentNext.next
                currentNext = None
                currentNext = current.next
            current = current.next

    def has_cycle(self, head):
        visited = {}
        current = head
        while current:
            if current in visited:
                return 1
            visited.setdefault(current, True)
            current = current.next
        return 0

    def FindMergeNode(self, headA, headB):
        
        curA = headA
        curB = headB
        while not curA == curB:
            if curA.next is None:
                curA = headB
            else:
                curA = curA.next
            if curB.next is None:
                curB = headA
            else:
                curB = curB.next
        return curA.data

    def pprint(self):
        d = []
        current = self.head
        while current:
            d.append(str(current.data))
            current = current.next
        d.append("NULL")
        print "->".join(d)

def la():
    l = LinkedList(1)
    l.addNode(2)            
    l.addNode(3)            
    l.addNode(4)            
    l.addNode(5)            
    l.addNode(6)
    return l

def lb():
    l2 = LinkedList(1)
    l2.addNode(2)            
    l2.addNode(3)            
    l2.addNode(4)            
    l2.addNode(5)            
    l2.addNode(6)
    return l2

def lc():
    l2 = LinkedList(1)
    l2.addNode(3)            
    l2.addNode(5)            
    l2.addNode(6)            
    return l2

def ld():
    l2 = LinkedList(2)
    l2.addNode(4)            
    l2.addNode(7)            
    return l2

def le():
    l2 = LinkedList(12)
    return l2

def lf():
    l2 = LinkedList(15)
    return l2

def lg():
    l2 = LinkedList(1)
    l2.addNode(1)            
    l2.addNode(2)            
    l2.addNode(2)            
    l2.addNode(2)            
    l2.addNode(3)            
    l2.addNode(3)            
    l2.addNode(3)            
    l2.addNode(4)            
    l2.addNode(4)            
    l2.addNode(5)            
    l2.addNode(6)            
    l2.addNode(6)            
    l2.addNode(7)            
    l2.addNode(7)            
    return l2

if __name__ == "__main__":
    l1 = la()
    l2 = lb()

    l3 = lc()
    l4 = ld()
    l5 = le()
    l6 = lf()
    #l.pprint() 
    #l.Reverse(l.head)
    #l.pprint()           

    #print l.CompareLists(None, None)
    #print l.CompareLists(l.head, l2.head)
    l3.MergeLists(l3.head, l4.head)
    l3.pprint()
    l5.MergeLists(l5.head, l6.head)
    l5.pprint()
    l1.MergeLists(None, l1.head)
    l1.pprint()
    
    l1 = la()
    l1.pprint()
    print l1.GetNode(l1.head, 3)

    l1 = lg()
    l1.pprint()
    l1.RemoveDuplicates(l1.head)
    l1.pprint()
    print l1.has_cycle(l1.head)
    
    l1.

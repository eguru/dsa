
import sys

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
      
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head


    def addNode(self, data):
        n = Node(data)
        self.tail.next = n
        self.tail = n
    
    def addHead(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n   
    
    def getPrevious(self, node):
        current = self.head
        previous = None
        while current.next and current != node:
            previous = current
            current = current.next
        return previous

    def _addNumber(self, node, d):
        
        if d:
            # add value to current node and send carry to
            # previous
            val = str(node.data + d)
            node.data = val[-1]
            carry = 0
            if len(val) > 1:
                carry = int(val[0:-1])
                previous = self.getPrevious(node)
                if previous:
                    self._addNumber(previous, carry)
                else:
                    print "Carry: ", carry
                    # for each digit in carry add new node
                    # in head
                    for new_data in reversed(str(carry)):
                        self.addHead(int(new_data))
        
    def addNumber(self, head, d):
        self._addNumber(self.tail,d)
        
    def pprint(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        nodes.append("null")
        print " -> ".join(nodes)

if __name__ == "__main__":
    
    ll = LinkedList(1)
    ll.addNode(2)
    ll.addNode(3)
    ll.addNode(4)
    ll.addNode(5)
    ll.addNode(6)
    ll.addNode(7)
    ll.addNode(8)

    #ll.getPrevious(ll.head.next.next.next) # 1 -> 2 -> 3 -> 4
    #ll.getPrevious(ll.head.next.next.next.next.next) # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    #ll.getPrevious(ll.head) # 1
    #ll.getPrevious(ll.head.next.next.next.next.next.next.next) # 1 -> 2 -> .... -> 8 

    ll.pprint()
    print "Tail: ", ll.tail.data

    #ll.addNumber(ll.head, 50)
    ll.addNumber(ll.head, int(sys.argv[1]))
    
    ll.pprint()
    print "Tail: ", ll.tail.data

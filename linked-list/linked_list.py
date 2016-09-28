import math

class LinkedList(object):
    def __init__(self, head=None):
         self.head = head
    
    def insert(self, node):
        node.set_next(self.head)
        self.head = node

    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.get_next()
        return size    

    def get_middle(self):
          size = self.size()
          mid = math.ceil(size/2.0)
          # even
          if size % 2 == 0:
              mid += 1
          i = 1
          current = self.head
          while current and i < mid:
               current = current.get_next()
               i += 1

          return current.get_data()

    def pprint(self):
        current = self.head
        while current:
            print current.get_data(), 
            current = current.get_next()
        print

class Node(object):
    
    def __init__(self, data, next_node=None):
        
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
   
    def get_next(self):
        return self.next_node

    def set_data(self, d):
        self.data = d

    def set_next(self, next_node):
        self.next_node = next_node

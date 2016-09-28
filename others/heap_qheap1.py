

class Node(data, left=None, right=None):
    self.left = left
    self.right = right
    self.data = data

class MinHeap(object):
    
    def __init__(self, root):
        self.root = root
    
    def addNode(self, node, data):
        if not node:
            return
        if not node.left:
            n = Node(data)
            node.left = n
        elif not node.right:
            node.right = n
        else:
            

for i in range(int(raw_input())):
    cmd = [int(i.strip()) for i in raw_input().split() if i.strip()]
    if len(cmd) == 1:
        val = None
    else:
        cmd, val = cmd

    if cmd == 1:
        

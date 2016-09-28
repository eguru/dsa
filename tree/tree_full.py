class Node(object):
    
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

class Tree(object):
    
    def __init__(self, d):
        self.root = Node(d, None)

    def addNode(self, node, d):
        
        if d >= node.data:
            if not node.right:
                node.right = Node(d, node)
            else:
                self.addNode(node.right, d)
        elif d < node.data:
            if not node.left:
                node.left = Node(d, node)
            else:
                self.addNode(node.left, d)

    def preOrder(self, node, t):
        if node:
            print t, node.data, 
            self.preOrder(node.left, "L")
            self.preOrder(node.right, "R")        

    def postOrder(self, node, t):
        if node:
            self.postOrder(node.left, "L")
            self.postOrder(node.right, "R")        
            print t, node.data, 

    def inOrder(self, node, t):
        if node:
            self.inOrder(node.left, "L")
            print t, node.data, 
            self.inOrder(node.right, "R")        

    def _left(self, node):
        if node:
            self._left(node.left)
            print node.data, 

    def _right(self, node):
        if node:
            print node.data, 
            self._right(node.right)

    def treeView(self, node, t):
        if node:
            self._left(node.left)
            print node.data, 
            self._right(node.right)


    def maxDepth(self, root):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))    
    
    def height(self, node):
        if not node:
            return -1

        ld = self.maxDepth(node.left)
        rd = self.maxDepth(node.right)
        if ld > rd:
            return ld + 1
        else:
            return rd + 1

    def levelOrder(self, root):
        def _printLevelOrder(self, node, level):
            if not node:
                return None
            if level == 1:
                print node.data, 
            else:
                _printLevelOrder(self, node.left, level-1) 
                _printLevelOrder(self, node.right, level-1) 
        h = self.height(root) + 1
        for i in range(1, h+1):
            _printLevelOrder(self, root, i) 
 
    def levelOrderQueue(self, root):
        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            print node.data, 
            if node and node.left:
                queue.append(node.left)
            if node and node.right:
                queue.append(node.right)

    def Insert(self, root, val):
        if not root:
            return None
        
        if val < root.data:
            #left
            if root.left:
                self.Insert(root.left, val)
            else:
                n = Node(val, root)
                root.left = n
        else:
            #right
            if root.right:
                self.Insert(root.right, val)
            else:
                n = Node(val, root)
                root.right = n
        return root

    def isLeaf(self, node):
        return (node and not node.left and not node.right)


    def huffman_decode(self, s, root):
        def _move(direction, node):
            if node and direction == "0":
                current = node.left
                #print "0: ", current.data
            elif node and direction == "1":
                current = node.right
                #print "1: ", current.data
            else:
                #print "-1: ", direction
                current = node
            return current

        node = root
        tmp_s = list(s)
        decoded_s = ""
        while tmp_s:
            while node and not self.isLeaf(node):
                node = _move(tmp_s.pop(0), node)
            if node and self.isLeaf(node):
                decoded_s += node.data
                node = root #_move(tmp_s.pop(0), root)
        return decoded_s


    def leastCommonAncestor(self, root, v1, v2):
        
        def _findAllAncestors(root, v):
            if not root:
                return None
            current= root
            v_ancestors = [] 
            while current:
                if v < current.data:
                    v_ancestors.append(current)
                    current = current.left 
                elif v > current.data:
                    v_ancestors.append(current)
                    current = current.right
                else:
                    break;
            return v_ancestors

        v1_ancestors = _findAllAncestors(root, v1)
        v2_ancestors = _findAllAncestors(root, v2)
        lca = [v for v in v1_ancestors if v in v2_ancestors]
        if lca:
            return lca[-1]
        else:
            return root

def t1():
    three = Node(3, None)
    five = Node(5, three)
    two = Node(2, three)
    three.left = five
    three.right = two
    one = Node(1, five)
    four = Node(4, five)
    six = Node(6, two)
    five.left = one
    five.right = four
    two.left = six
    return three

def t2():
    t = Tree(5)
    five = t.root
    two = Node(2, five)
    a = Node("A", five)
    b = Node("B", two)
    c = Node("C", two)
    five.left = two
    five.right = a
    two.left = b
    two.right = c
    return t

def t3():
    t = Tree(1)
    one = t.root
    two =   Node(2, one)
    three = Node(3, two)
    four =  Node(4, three)
    five =  Node(5, four)
    six =   Node(6, five)
    one.right = two
    two.left = three
    three.right = four
    four.left = five
    five.right = six
    return t


def main1():
    t = Tree(3)
    t.addNode(t.root, 5)
    t.addNode(t.root, 2)
    t.addNode(t.root, 1)
    t.addNode(t.root, 4)
    t.addNode(t.root, 6)
    print "PreOrder : ", 
    t.preOrder(t.root, "N")
    print
    print "PostOrder : ", 
    t.postOrder(t.root, "N")
    print
    print "InOrder : ", 
    t.inOrder(t.root, "N")
    print
    print "Height : ", t.height(t.root)
    print "Depth : ", t.maxDepth(t.root)
    print "Tree top View : ", t.treeView(t.root, "N")
    print
    t.levelOrder(t.root)
    print
    t.levelOrderQueue(t.root)
    print
    r = t.Insert(t.root, 11)
    print "Insert PreOrder : ", 
    t.preOrder(r, "N")
    print
    lca = t.leastCommonAncestor(t.root, 2, 6)
    print "Least Common Ancestor of 2 and 6: ", lca.data
    lca = t.leastCommonAncestor(t.root, 4, 6)
    print "Least Common Ancestor of 4 and 6: ", lca.data
    lca = t.leastCommonAncestor(t.root, 1, 2)
    print "Least Common Ancestor of 1 and 2: ", lca.data
    

def main2():
    print
    t = t2()
    print "Insert PreOrder : ", 
    t.inOrder(t.root, "N")
    print
    print "Huffman Decode : "
    print t.huffman_decode("1001011", t.root) 

def main3():
    print
    t = t3()
    print "InOrder : ", 
    t.inOrder(t.root, "N")
    

if __name__ == "__main__":
    #main1()
    #main2()
    main3()

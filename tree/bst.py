#!/usr/bin/env python
import sys

class Node(object):
    
    def __init__(self, value, left, right, parent):
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent
        
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getLeftChild(self):
        return self.left_child

    def setLeftChild(self, node):
        self.left_child = node

    def getRightChild(self):
        return self.right_child

    def setRightChild(self, node):
        self.right_child = node

    def isRoot(self):
        return not self.parent 

    def hasLeftChild(self):
        return self.left_child != None

    def hasRightChild(self):
        return self.right_child != None

    def isLeaf(self):
        return (not self.getLeftChild() and not self.getRightChild())    

    def setParent(self, parent):
        self.parent = parent
    
class BST(object):
    
    def __init__(self, root_val):
        self.root = Node(root_val, None, None, None)
        self.depth = 0

    def addNode(self, currNode, val):
        if val < currNode.getValue():
            if not currNode.hasLeftChild():
                currNode.setLeftChild(Node(val, None, None, currNode))
            else:
                self.addNode(currNode.getLeftChild(), val)
        else:
            if not currNode.hasRightChild():
                currNode.setRightChild(Node(val, None, None, currNode))
            else:
                self.addNode(currNode.getRightChild(), val)

    def maxDepth(self, node):
        if not node:
            return 0

        ld = self.maxDepth(node.getLeftChild())
        rd = self.maxDepth(node.getRightChild())
        if ld > rd:
            return ld + 1
        else:
            return rd + 1    

    def height(self, node):
        if not node:
            return 0

        return 1 + max(self.height(node.getLeftChild()), self.height(node.getRightChild()))

    def preOrderDFS(self, node):
        
        if node:
            print "Node: ", node.getValue()
            self.preOrderDFS(node.getLeftChild())
            self.preOrderDFS(node.getRightChild())

    def inOrderDFS(self, node):
        
        if node:
            self.inOrderDFS(node.getLeftChild())
            print "Node: ", node.getValue()
            self.inOrderDFS(node.getRightChild())

    def postOrderDFS(self, node):
        
        if node:
            self.postOrderDFS(node.getLeftChild())
            self.postOrderDFS(node.getRightChild())
            print "Node: ", node.getValue()

    def isBalanced(self, node):
        if not node:
            return True
        
        lh = self.height(node.getLeftChild())
        rh = self.height(node.getRightChild())
   
        if abs(lh - rh) <= 1 \
            and self.isBalanced(node.getLeftChild())\
            and self.isBalanced(node.getRightChild()):
            return True
        print lh, rh, abs(lh - rh)
        return False

    def getRoot(self):
        return self.root

def createNumberTree():
    bst = BST(16)
    root = bst.getRoot()
    bst.addNode(root, 12)
    bst.addNode(root, 50)
    bst.addNode(root, 7)
    bst.addNode(root, 14)
    bst.addNode(root, 40)
    bst.addNode(root, 60)
    bst.addNode(root, 5)
    bst.addNode(root, 10)
    bst.addNode(root, 13)
    bst.addNode(root, 15)
    bst.addNode(root, 20)
    bst.addNode(root, 45)
    bst.addNode(root, 48)
    bst.addNode(root, 70)
    bst.addNode(root, 43)
    bst.addNode(root, 55)
    return bst    

def createNumberTreeSmall():
    bst = BST(15)
    root = bst.getRoot()
    bst.addNode(root, 10)
    bst.addNode(root, 20)
    bst.addNode(root, 18)
    bst.addNode(root, 25)
    return bst

def createAlphaTree():
    bst = BST("F")
    root = bst.getRoot()
    bst.addNode(root, "B")
    bst.addNode(root, "G")
    bst.addNode(root, "A")
    bst.addNode(root, "D")
    bst.addNode(root, "I")
    bst.addNode(root, "C")
    bst.addNode(root, "E")
    bst.addNode(root, "H")
    return bst

def createAlphaTree2():
    bst = BST("A")
    root = bst.getRoot()
    bst.addNode(root, "F")
    bst.addNode(root, "D")
    bst.addNode(root, "E")
    bst.addNode(root, "B")
    bst.addNode(root, "C")
    return bst
 
def createNumberTree2():
    bst = BST(50)
    root = bst.getRoot()
    bst.addNode(root, 30)
    bst.addNode(root, 70)
    bst.addNode(root, 20)
    bst.addNode(root, 40)
    bst.addNode(root, 60)
    bst.addNode(root, 80)
    bst.addNode(root, 5)
    bst.addNode(root, 25)
    bst.addNode(root, 48)
    bst.addNode(root, 45)
    bst.addNode(root, 22)
    return bst

if __name__ == "__main__":
    if sys.argv[1] == "n":
        tree = createNumberTree()
    elif sys.argv[1] == 's':
        tree = createNumberTreeSmall()
    elif sys.argv[1] == '2':
        tree = createNumberTree2()
    elif sys.argv[1] == 'a2':
        tree = createAlphaTree2() 
    else:
        tree = createAlphaTree() 

    print "PreOrder DFS:"
    tree.preOrderDFS(tree.getRoot())
    print "InOrder DFS:"
    tree.inOrderDFS(tree.getRoot())
    print "PostOrder DFS:"
    tree.postOrderDFS(tree.getRoot())

    print "Max Depth"
    print tree.maxDepth(tree.getRoot())
    print "Tree Height"
    print tree.height(tree.getRoot())
    print "Is tree Balanced: ", tree.isBalanced(tree.getRoot())

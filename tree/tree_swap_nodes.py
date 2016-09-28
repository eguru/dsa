class Node(object):
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

class BTree(object):
    
    def __init__(self, root):
        self.root = root

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print root.data, 
        self.inOrder(root.right)

    def swap_subtree_at_depth(self, node, current_depth, depth):
        if node and current_depth == depth:
            self._swap_subtree(node)
        else:
            if node and node.left:
                self.swap_subtree_at_depth(node.left, current_depth+1, depth)
            if node and node.right:
                self.swap_subtree_at_depth(node.right, current_depth+1, depth)

    def max_depth(self, node):
        if not node:
            return 0
        ld = self.max_depth(node.left)
        rd = self.max_depth(node.right)
        if ld > rd:
            return ld + 1
        else:
            return rd + 1

    def _swap_subtree(self, node):
        node.left, node.right = node.right, node.left

def main():
    root = Node(1)
    tree = BTree(root)
    nodes = [root]
    for i in range(int(raw_input().strip())):
        ld, rd = map(int, raw_input().split())
        if ld >= 0:
            nodes[i].left = Node(ld)
            nodes.append(nodes[i].left)
        if rd >= 0:
            nodes[i].right = Node(rd)
            nodes.append(nodes[i].right)
    #print [n.data for n in nodes]
    #tree.inOrder(root)
    tree_depth = tree.max_depth(root)
    print "tree depth: ", tree_depth
    for i in range(int(raw_input().strip())):
        k = int(raw_input().strip())
        while k <= tree_depth:
            #print "Depth: ", 1, k, tree_depth
            tree.swap_subtree_at_depth(root, 1, k)
            #tree.inOrder(root)
            #print
            k *= 2
        tree.inOrder(root)
        print

if __name__ == "__main__":
    main()         

"""
def Insert(self, root, val):
    if not root:
        n = Node(val, None)
        root = n
        return root

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
"""
static Node Insert(Node root,int value)
{
    if (root != null) {
        if (value < root.data) {
            if (root.left != null) {
                Insert(root.left, value);
            } else {
                Node n = new Node();
                n.data = value;
                n.left = null;
                n.right = null;
                root.left = n;
            }
        } else {
            if (root.right != null) {
                Insert(root.right, value);
            } else {
                Node n = new Node();
                n.data = value;
                n.left = null;
                n.right = null;
                root.right = n;
            }
        }
    } else {
        Node n = new Node();
        n.data = value;
        n.left = null;
        n.right = null;
        root = n;
    }
    return root;      
}

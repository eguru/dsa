"""
void top_left(Node node)
{
    if (node != null)
    {
        top_left(node.left);
        System.out.print(node.data + " ");
    }
}

void top_right(Node node)
{
    if (node != null)
    {
        System.out.print(node.data + " ");
        top_right(node.right);
    }
}

void top_view(Node root)
{
    if (root != null)
    {
        top_left(root.left);
        System.out.print(root.data + " ");
        top_right(root.right);
    }
}
"""
def _left(self, node):
    if node:
        self._left(node.left)
        print node.data

def _right(self, node):
    if node:
        print node.data
        self._right(node.right)

def treeView(self, node, t):
    if node:
        self._left(node.left)
        print node.data
        self._right(node.right)


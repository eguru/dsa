"""
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
"""
void LevelOrder(Node root)
{
    if (root != null) {
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node n = queue.remove();
            System.out.print(n.data + " ");
            if (n.left != null) {
                queue.add(n.left);
            }
            if (n.right != null) {
                queue.add(n.right);
            }
        }
    }
}

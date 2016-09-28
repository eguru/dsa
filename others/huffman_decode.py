"""
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
"""
Node move(String ch, Node node)
{
    Node current = node;
    if (node != null && ch.equals("0") == true)
    {
        current = node.left;
    }
    else if (node != null && ch.equals("1") == true)
    {
        current = node.right;
    }
    return current;
}

boolean isLeaf(Node node)
{
    return (node != null && node.left == null && node.right == null);
}

void decode(String S ,Node root)
{
    Node node = root;
    String decodedString = "";
    while (S.length() > 0)
    {
        while (node != null && isLeaf(node))
        {
            String ch = S.substring(0, 1);
            S = S.substring(1);
            node = move(ch, node);
        }
        if (node != null && isLeaf(node))
        {
            decodedString += node.data;
            node = root;
        }
    }
    System.out.print(decodedString);
}


class Node
{
    public  int frequency; // the frequency of this tree
    public  String data;
    public  Node left, right;
   
    public Node(String data, Node left, Node right)
    {
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

class BST
{
    public BST() {}

    public Node move(String ch, Node node)
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

    public boolean isLeaf(Node node)
    {
        return (node != null && node.left == null && node.right == null);
    }

    public void decode(String S ,Node root)
    {
        Node node = root;
        String decodedString = "";
        while (S.length() > 0)
        {
            while (node != null && !isLeaf(node))
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

}


public class HuffmanDecode 
{
    public static void main(String[] args) 
    {
    
        Node A = new Node("A", null, null);
        Node B = new Node("B", null, null);
        Node C = new Node("C", null, null);
        Node two = new Node("2", B, C);
        Node root = new Node("5", two, A);
        BST bst = new BST();
        bst.decode("1001011", root);             

    }
}

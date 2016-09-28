import java.util.ArrayList;
import java.util.List;
class Node
{
    public  int frequency; // the frequency of this tree
    public  int data;
    public  Node left, right;
   
    public Node(int data, Node left, Node right)
    {
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

class BST
{
    public BST() {}
    
    public List<Node> getAncestors(Node root, int v)
    {
        List<Node> ancestors = new ArrayList<Node>();
        Node current = root;
        boolean found = false;
        while (current != null) {
            if (v < current.data) {
                ancestors.add(current);
                current = current.left;
            } else if (v > current.data) {
                ancestors.add(current);
                current = current.right;
            }
            else {
                if (current == root) {
                    ancestors.add(root);
                }
                found = true;
                break;
            }
        }
        if (!found) {
            return new ArrayList<Node>();
        }
        return ancestors;
    }

    public Node lca2(Node root, int v1, int v2)
    {
        List<Node> v1_ancestors = getAncestors(root, v1);
        List<Node> v2_ancestors = getAncestors(root, v2);
        //System.out.println(v1_ancestors.toString());
        //System.out.println(v2_ancestors.toString());

        v1_ancestors.retainAll(v2_ancestors);
        Node ancestor = null;
        if (v1_ancestors.size() > 0) {
            ancestor = v1_ancestors.get(v1_ancestors.size() -1);
        }
        return ancestor;
    }

    public Node lca(Node root, int v1, int v2)
    {
        if (root == null) {
            return null;
        }

        if (v1 < root.data && v2 < root.data) {
            return lca(root.left, v1, v2);
        } else if (v1 > root.data && v2 > root.data) {
            return lca(root.right, v1, v2);
        }
        return root;
    }

}


public class LeastCommonAncestor
{
    public static void main(String[] args) 
    {
    
        Node one = new Node(1, null, null);
        Node four = new Node(4, null, null);
        Node ten = new Node(10, null, null);
        Node six = new Node(6, null, ten);
        Node two = new Node(2, one, null);
        Node five = new Node(5, four, six);
        Node root = new Node(3, two, five);
        BST bst = new BST();
        Node ancestor = bst.lca(root, 2, 5);
        if (ancestor != null)
        {
            System.out.println ("Least common ancestor 2 5: " + ancestor.data);
        }
        ancestor = bst.lca(root, 2, 10);
        if (ancestor != null)
        {
            System.out.println ("Least common ancestor 2 10: " + ancestor.data);
        }
        ancestor = bst.lca(root, 4, 6);
        if (ancestor != null)
        {
            System.out.println ("Least common ancestor 4 6: " + ancestor.data);
        }
        ancestor = bst.lca(root, 3, 3);
        if (ancestor != null)
        {
            System.out.println ("Least common ancestor 3 3: " + ancestor.data);
        }
        ancestor = bst.lca(root, -1, 100);
        if (ancestor != null)
        {
            System.out.println ("Least common ancestor -1 100: " + ancestor.data);
        }
    }
}

import java.util.*;
class Node{
    int data;
    Node left,right;
    Node(int data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
class BST{
    Node root;
    BST(){
        this.root = null;
    }
    void insert_root(int data){
        if(root == null) root = new Node(data);
        else insert_leaf(root,data);
    }
    void insert_leaf(Node root,int data){
        if(data < root.data){
            if(root.left == null){
                root.left=new Node(data);
            }
            else insert_leaf(root.left, data);
        }
        else{
            if(root.right == null){
                root.right = new Node(data);
            }
            else insert_leaf(root.right, data);
        }
    }
    void traversal(Node root,String s){
        if(root == null) return;

        if(root.left == null && root.right == null){
            int data = root.data;
            s += String.valueOf(data);
        }
    }
}
public class findPath {
    public static void main(String[] args) {
        String s="";
        BST bt = new BST();
        Scanner in = new Scanner(System.in);
        int n=in.nextInt();
        for(int i=0;i<n;i++){
            bt.insert_root(in.nextInt());
        }
        bt.traversal(bt.root,s);
        in.close();
    } 
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package assignment3;

/**
 *
 * @author LENOVO
 */
public class BSTree {

    Node root;

    public BSTree() {
        root = null;
    }

    // boolean isEmpty()
    public boolean isEmpty() {
        return root == null;
    }

    public void visit(Node p) {
        if (p == null) {
            return;
        }
        System.out.print(p.info + "  ");
    }

    // void clear() 
    public void clear() {
        root = null;
    }

    //Node search(int x)
    public Node search(Node p, int x) {
        if (p == null) {
            return null;
        }
        if (p.info == x) {
            return p;
        } else if (p.info > x) {
            return search(p.left, x);
        } else {
            return search(p.right, x);
        }
    }

    // void insert(int x) 
    public void insert(int x) {
        Node p = new Node(x);
        Node f = null, q = root;
        while (q != null) {
            if (q.info == x) {
                System.out.println("Key cannot be duplicated...");
                return;
            }
            if (q.info < x) {
                f = q;
                q = q.right;
            } else {
                f = q;
                q = q.left;
            }
        }
        if (f == null) {
            root = p;
        } else if (p.info > f.info) {
            f.right = p;
        } else {
            f.left = p;
        }
    }

    // void breadth()
    public void BFT(Node p) {
        if (p == null) {
            return;
        }
        MyQueue m = new MyQueue();
        m.enqueue(p);
        while (!m.isEmpty()) {
            Node q = (Node) m.dequeue();
            visit(q);
            if (q.left != null) {
                m.enqueue(q.left);
            }
            if (q.right != null) {
                m.enqueue(q.right);
            }
        }
    }
    //preorder a tree

    public void preOrder(Node p) {
        if (p == null) {
            return;
        }
        visit(p);
        preOrder(p.left);
        preOrder(p.right);
    }

    //postorder a tree
    public void postOrder(Node p) {
        if (p == null) {
            return;
        }
        postOrder(p.left);
        postOrder(p.right);
        visit(p);
    }

    //inorder a tree
    public void inOrder(Node p) {
        if (p == null) {
            return;
        }
        inOrder(p.left);
        visit(p);
        inOrder(p.right);
    }
    //int count()
    public int count(Node p){
         if (p == null) {
            return 0;
        }
        return 1 + count(p.left) + count(p.right);
    }
    //void dele(int x)
    public void delete(int x) {
        Node p = search(root, x);
        if (p == null) {
            System.out.println("Key " + x + " does not exists, deletion failed");
            return;
        }
        //find f is father of p
        Node f = null, q = root;
        while (q != p) {
            f = q;
            if (q.info > p.info) {
                q = q.left;
            } else {
                q = q.right;
            }
        }
        //1.p has no child
        if (p.left == null && p.right == null) {
            if (f == null) {
                root = null;
            } else if (f.left == p) {
                f.left = null;
            } else {
                f.right = null;
            }
        } //2.p has left child only
        else if (p.left != null && p.right == null) {
            if (f == null) {
                root = p.left;
            } else if (f.left == p) {
                f.left = p.left;
            } else {
                f.right = p.left;
            }
        } //3.p has right child only
        else if (p.left == null && p.right != null) {
            if (f == null) {
                root = p.right;
            } else if (f.left == p) {
                f.left = p.right;
            } else {
                f.right = p.right;
            }
        } //4.p has both child
        else if (p.left != null && p.right != null) {
            //tim q la node lon nhat ben con trai cua p -> q la con phai nhat
            //cua con trai cua p
            q = p.left;
            f = null;
            while (q.right != null) {
                f = q;
                q = q.right;
            }
            p.info = q.info;
            //delete q
            if (f == null) {
                p.left = q.left;
            } else {
                f.right = q.left;
            }
        }
    }
    //min 
     void minVlaue(Node p) {
        Node min = p;
        while (min.left != null) {
            min = min.left;
        }
        visit(min);
    }
     //max
    void maxVlaue(Node p) {
        Node max = p;
        while (max.right != null) {
            max = max.right;
        }
        visit(max);
    }
    // sum
    int sum(Node p) {
        if (p == null) {
            return 0;
        }
        return p.info + sum(p.left) + sum(p.right);
    }
    //avg
    int avg(Node p) {
        return sum(p) / count(p);
    }

    //height of tree
    int height(Node p)
    {if(p==null) {return 0;}
    else{int lDepth=height(p.left);//compute the depth of each subtree
    int rDepth=height(p.right);
    if (lDepth > rDepth) return (lDepth + 1);//use the larger one
    else return (rDepth + 1);
    }}

}

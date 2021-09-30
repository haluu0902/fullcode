
import java.util.ArrayList;
import java.util.Collections;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
class BinTree {
    Node root;
    public void reBalance(){
        ArrayList<Integer> list = new ArrayList();
        
        if(root == null)    return;
        MyQueue q = new MyQueue();
        q.enQueue(root);
        while(!q.isEmpty()){
            Node p = (Node)q.deQueue();
            if(p.left != null) q.enQueue(p.left);
            if(p.right != null) q.enQueue(p.right); 
            list.add(p.info);
        }
        
        root = null;
        Collections.sort(list);
        int a[] = new int[list.size()];
        for(int i=0;i<list.size();i++)  
            a[i] = list.get(i);
        this.balance(a);
    }
    public void balance(int data[], int first, int last) {
        if (first <= last) {
            int middle = (first + last) / 2;
            insert(data[middle]);
            balance(data, first, middle - 1);
            balance(data, middle + 1, last);
        }
    }
    public void balance(int data[]) {
        balance(data, 0, data.length - 1);
    }

    public void inOrder(){  this.inOrder(root);     }
    void insert(int x) {
        if (root == null) {
            root = new Node(x);
            return;
        }
        Node f, p;
        p = root;
        f = null;
        while (p != null) {
            if (p.info == x) {
                System.out.println(" The key " + x + " already exists, no insertion");
                return;
            }
            f = p;
            if (x < p.info) {
                p = p.left;
            } else {
                p = p.right;
            }
        }
        if (x < f.info) {
            f.left = new Node(x);
        } else {
            f.right = new Node(x);
        }
    }

    public void visit(Node x){
        System.out.print(x.info + ", ");
    }
    public void inOrder(Node v){
        if(v==null) return;
        inOrder(v.left);
        visit(v);
        inOrder(v.right);
    }
    public int count(){
        int count=0;
        if(root == null)    return 0;
        MyQueue q = new MyQueue();
        q.enQueue(root);
        while(!q.isEmpty()){
            Node p = (Node)q.deQueue();
            if(p.left != null) q.enQueue(p.left);
            if(p.right != null) q.enQueue(p.right); 
            //visit(p);
            count++;
        }
        return count;
    }
    public void breadthTraverse(){
        if(root == null)    return;
        MyQueue q = new MyQueue();
        q.enQueue(root);
        while(!q.isEmpty()){
            Node p = (Node)q.deQueue();
            if(p.left != null) q.enQueue(p.left);
            if(p.right != null) q.enQueue(p.right); 
            visit(p);
        }
    }
}

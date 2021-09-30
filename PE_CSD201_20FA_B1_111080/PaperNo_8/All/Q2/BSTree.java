/* This program contains 2 parts: (1) and (2)
   YOUR TASK IS TO COMPLETE THE PART  (2)  ONLY
 */
//(1)==============================================================
import java.io.*;
import java.util.*;

public class BSTree {
   Node root;
   BSTree() {root=null;}
   boolean isEmpty() {
       return(root==null);
      }
   void clear() {
       root=null;
      }
   void visit(Node p) {
      System.out.print("p.info: ");
      if(p != null) System.out.println(p.info + " ");
     }
   void fvisit(Node p, RandomAccessFile f) throws Exception {
      if(p != null) f.writeBytes(p.info + " ");
     }
   void preOrder(Node p, RandomAccessFile f) throws Exception {
      if(p==null) return;
      fvisit(p,f);
      preOrder(p.left,f);
      preOrder(p.right,f);
     }
   void inOrder(Node p, RandomAccessFile f) throws Exception {
      if(p==null) return;
      inOrder(p.left,f);
      fvisit(p,f);
      inOrder(p.right,f);
     }
   void postOrder(Node p, RandomAccessFile f) throws Exception {
      if(p==null) return;
      postOrder(p.left,f);
      postOrder(p.right,f);
      fvisit(p,f);
     }
  void breadth(Node p, RandomAccessFile f) throws Exception {
     if(p==null) return;
     Queue q = new Queue();
     q.enqueue(p);Node r;
     while(!q.isEmpty()) {
        r = q.dequeue();
        fvisit(r,f);
        if(r.left!=null) q.enqueue(r.left);
        if(r.right!=null) q.enqueue(r.right);
       }
    }
   void loadData(int k) { //do not edit this function
      String [] a = Lib.readLineToStrArray("data.txt", k);
      int [] b = Lib.readLineToIntArray("data.txt", k+1);
      int [] c = Lib.readLineToIntArray("data.txt", k+2);
      int n = a.length;
      for(int i=0;i<n;i++) insert(a[i],b[i],c[i]);
     }

//===========================================================================
//(2)===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
//===========================================================================
  void insert(String xMaker, int xType, int xRadius) {
    //You should insert here statements to complete this function
    if(xMaker.charAt(0) == 'B'){}
    else{
      Ball x = new Ball(xMaker, xType, xRadius);
      Node q=new Node(x);
      if(isEmpty())
        {root=q;
          return;
        }
      Node f,p;
      f=null;p=root;
      while(p!=null)
        {if(p.info.type == x.type)
            {System.out.println("The key " + x.type + " already exists, no insertion");
              return;
            }
          f=p;
          if(x.type < p.info.type) p=p.left; else p=p.right;
        } 
        if(x.type< f.info.type) f.left=q; else f.right=q;
      }
   }

//Do not edit this function. Your task is to complete insert function above only.
  void f1() throws Exception {
    clear();
    loadData(1);
    String fname = "f1.txt";
    File g123 = new File(fname);
    if(g123.exists()) g123.delete();
    RandomAccessFile  f = new RandomAccessFile(fname, "rw"); 
    breadth(root,f);
    f.writeBytes("\r\n");
    inOrder(root,f);
    f.writeBytes("\r\n");
    f.close();
   }  
  
//=============================================================
  void f2() throws Exception {
    clear();
    loadData(5);
    String fname = "f2.txt";
    File g123 = new File(fname);
    if(g123.exists()) g123.delete();
    RandomAccessFile  f = new RandomAccessFile(fname, "rw"); 
    postOrder(root,f);
    f.writeBytes("\r\n");
    //------------------------------------------------------------------------------------
    /*You must keep statements pre-given in this function.
      Your task is to insert statements here, just after this comment,
      to complete the question in the exam paper.*/
      postOrder2(root,f);


    //------------------------------------------------------------------------------------
    f.writeBytes("\r\n");
    f.close();
   }
   void postOrder2(Node p, RandomAccessFile f) throws Exception {
    if(p==null) return;      
      postOrder2(p.left,f);
      postOrder2(p.right,f); 
      if(p.info.radius < 5){
        fvisit(p,f);
      }
   }  

//=============================================================
  void f3() throws Exception {
    clear();
    loadData(9);
    String fname = "f3.txt";
    File g123 = new File(fname);
    if(g123.exists()) g123.delete();
    RandomAccessFile  f = new RandomAccessFile(fname, "rw"); 
    breadth(root,f);
    f.writeBytes("\r\n");
    //------------------------------------------------------------------------------------
    /*You must keep statements pre-given in this function.
      Your task is to insert statements here, just after this comment,
      to complete the question in the exam paper.*/
      Node p = root;
      Queue m = new Queue();
        m.enqueue(p);
        while(!m.isEmpty()) {
          Node q = (Node)m.dequeue();
          if(q.left != null) m.enqueue(q.left);
          if(q.right != null) m.enqueue(q.right);
          if(q.left != null && q.right != null){
            remove(q);
            break;
          }
      }

    //------------------------------------------------------------------------------------
    breadth(root,f);
    f.writeBytes("\r\n");
    f.close();
   }  

    public void remove(Node p) {
      if (isEmpty()) {
          return;
      }
      if(p == null){
          System.out.println("Key does not exists, deletion failed");
          return;
      }
      // Find Node f where f is father of p
      Node f = null;
      Node q = root;
      while(q != p){
        if(q.info.type == p.info.type) break;
          if(q.info.type > p.info.type){
              f = q;
              q = q.left;
          }
          else{
              f = q;
              q = q.right;
          }
      }
      if(p.left != null && p.right != null){
          f = null;
          Node rp = p.left;
          while(rp.right != null){
              f = rp;
              rp = rp.right;
          }
          p.info = rp.info;
          if(f == null){// rp has no right child 
              p.left = rp.left;
          }
          else{
              f.right = rp.left;
          }
      }
}

//=============================================================
  void f4() throws Exception {
    clear();
    loadData(13);;
    String fname = "f4.txt";
    File g123 = new File(fname);
    if(g123.exists()) g123.delete();
    RandomAccessFile  f = new RandomAccessFile(fname, "rw"); 
    breadth(root,f);
    f.writeBytes("\r\n");
    //------------------------------------------------------------------------------------
    /*You must keep statements pre-given in this function.
      Your task is to insert statements here, just after this comment,
      to complete the question in the exam paper.*/
 

     
    //------------------------------------------------------------------------------------
    breadth(root,f);
    f.writeBytes("\r\n");
    f.close();
   }  

 }

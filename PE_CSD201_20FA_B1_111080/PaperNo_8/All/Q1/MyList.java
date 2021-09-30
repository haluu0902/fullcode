/* This program contains 2 parts: (1) and (2)
   YOUR TASK IS TO COMPLETE THE PART  (2)  ONLY
 */
//(1)==============================================================
import java.util.*;
import java.io.*;

public class MyList {
  Node head,tail;
  MyList() {head=tail=null;}
  boolean isEmpty() {
    return(head==null);
   }
  void clear() {head=tail=null;}

  void fvisit(Node p, RandomAccessFile f) throws Exception {
    if(p != null) f.writeBytes(p.info + " ");
   }

  void ftraverse(RandomAccessFile f) throws Exception {
    Node p = head;
    while(p!=null) {
       fvisit(p,f); // You will use this statement to write information of the node p to the file
       p=p.next;
      }
    f.writeBytes("\r\n");
   }

  void loadData(int k) { //do not edit this function
    String [] a = Lib.readLineToStrArray("data.txt", k);
    int [] b = Lib.readLineToIntArray("data.txt", k+1);
    int [] c = Lib.readLineToIntArray("data.txt", k+2);
    int n = a.length;
    for(int i=0;i<n;i++) addLast(a[i],b[i],c[i]);
   }

//===========================================================================
//(2)===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
//===========================================================================
/* 
   Khong su dung tieng Viet co dau de viet ghi chu.
   Neu dung khi chay truc tiep se bao loi va nhan 0 diem
*/
  void addLast(String xMaker, int xType, int xRadius) {
    //You should write here appropriate statements to complete this function.
    if(xMaker.charAt(0)== 'A'){}
    else{
      Node q = new Node(new Ball(xMaker, xType, xRadius));
      if(isEmpty()){
        head=tail=q;return;
      }
      tail.next=q;tail=q;
    }
   }

  //You do not need to edit this function. Your task is to complete the addLast function above only.
  void f1() throws Exception {
     clear();
     loadData(1);
     String fname = "f1.txt";
     File g123 = new File(fname);
     if(g123.exists()) g123.delete();
     RandomAccessFile  f = new RandomAccessFile(fname, "rw"); 
     ftraverse(f);
     f.close();
    }  

//==================================================================
  void f2() throws Exception {
     clear();
     loadData(5);
     String fname = "f2.txt";
     File g123 = new File(fname);
     if(g123.exists()) g123.delete();
     RandomAccessFile  f = new RandomAccessFile(fname, "rw"); 
     ftraverse(f);
     Ball x, y;
     x = new Ball("X",1,2);
     y = new Ball("Y",3,4);
     //------------------------------------------------------------------------------------
     /*You must keep statements pre-given in this function.
       Your task is to insert statements here, just after this comment,
       to complete the question in the exam paper.*/
       //insertPositionK(x,4);
       insertPositionK(x,4,y,3);


    //------------------------------------------------------------------------------------
     ftraverse(f);
     f.close();
    }
    public void insertPositionK(Ball x, int positionx, Ball y, int positiony) {
      if (isEmpty()) head = tail = new Node(x);
      int count = 1;
      Node p = head;
      Ball value1, value2;
      int position1 = 0;
      int position2 = 0;
      if(positionx < positiony){
        position1 = positionx;
        position2 = positiony;
        value1 = x;
        value2 = y;
      } 
      else{
        position1 = positiony;
        position2 = positionx;
        value1 = y;
        value2 = x;
      } 
      while (p!= null && count < position1-1) {
        p = p.next;
        count ++;
      }
      Node temp = p.next;
      p.next = new Node(value1, temp);
      while (p!= null && count < position2-1) {
        p = p.next;
        count ++;
      }
      Node temp1 = p.next;
      p.next = new Node(value2, temp1);
    }  

//==================================================================
  void f3() throws Exception {
    clear();
    loadData(9);
    String fname = "f3.txt";
    File g123 = new File(fname);
    if(g123.exists()) g123.delete();
    RandomAccessFile  f = new RandomAccessFile(fname, "rw"); 
    ftraverse(f);
    //------------------------------------------------------------------------------------
     /*You must keep statements pre-given in this function.
       Your task is to insert statements here, just after this comment,
       to complete the question in the exam paper.*/
      int max = getMaxPerson().radius;
      deleteSecondMax(max);


    //------------------------------------------------------------------------------------
    ftraverse(f);
    f.close();
   }
   public Ball getMaxPerson(){
    if(isEmpty()) return null;
    Ball max = head.info;                
    Node p = head;
    while( p != null){
        if(p.info.radius > max.radius) max = p.info;
        p = p.next;
    }
    return max; 
  }
  public void deleteSecondMax(int max){
		Node p = head;
		int count = 0;
		while(p != null){
			if(p.info.radius == max && count != 3) count ++;
			if(count == 2) break;
			p = p.next;
		}
		remove(p);
  }
  public void remove(Node p) 
    {if(p == null) return;
     Node f = head, q = null;
     while(f != null && f != p) {q = f; f = f.next;}
     if(q == null) {head = head.next;
        if(head == null) tail = null;
     }else {q.next = p.next;
       if(p == tail) tail = q;
     }
     p.next = null;
    }

//==================================================================
  void f4() throws Exception {
    clear();
    loadData(13);
    String fname = "f4.txt";
    File g123 = new File(fname);
    if(g123.exists()) g123.delete();
    RandomAccessFile  f = new RandomAccessFile(fname, "rw"); 
    ftraverse(f);
    //------------------------------------------------------------------------------------
     /*You must keep statements pre-given in this function.
       Your task is to insert statements here, just after this comment,
       to complete the question in the exam paper.*/
       sortf4element();



    //------------------------------------------------------------------------------------
    ftraverse(f);
    f.close();
   }
   public void sortf4element() {
    Node pi, pj; pi = head; int count = 0; 
    while(pi != null) {
        count++; pj = pi.next; int count1 = 0;
        while(pj != null) {
            count1++;
            if(pi.info.radius < pj.info.radius ) {
                Ball t = pi.info; 
                pi.info = pj.info;
                pj.info = t;
            }
            pj = pj.next; if(count1 == 4 - count) break;
        }
        pi = pi.next; if(count == 3) break;
    }
}
 }

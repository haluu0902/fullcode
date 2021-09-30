/* This program contains 2 parts: (1) and (2)
   YOUR TASK IS TO COMPLETE THE PART  (2)  ONLY
 */
//(1)==============================================================
import java.util.*;

public class MyList {
    Node head, tail;

    MyList() {
        head = tail = null;
    }

    boolean isEmpty() {
        return (head == null);
    }

    void clear() {
        head = tail = null;
    }
    
    void displayAll(){
        Node p = head;
        while (p != null) {
            System.out.print(p.info + " "); 
            p = p.next;
        }
        System.out.println("\r\n");
    }

//===========================================================================
//(2)===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
//===========================================================================
    
    void addLast(String xOwner, int xPrice) {
        if(xOwner.charAt(0) != 'B' && xPrice < 100){
            addToTail(xOwner, xPrice);
        }        
    }

    void f1() {/* You do not need to edit this function. Your task is to complete the addLast  function
        above only.
         */
        this.clear();
        String[] a = {"A", "B", "C", "D", "E", "F", "G"};
        int[] b =    {9,    3,   7,   2,   6,   4,  105};
        int n = a.length;
        for (int i = 0; i < n; i++) {
            addLast(a[i], b[i]);
        }        
        this.displayAll();
    }

//==================================================================
    void f2() {
        this.clear();
        String[] a = {"C", "D", "E", "F", "I"};
        int[] b =    {9,    6,   8,   2,   6};
        int n = a.length;
        for (int i = 0; i < n; i++) {
            addLast(a[i], b[i]);
        }
        this.displayAll();
        
        Car x = new Car("X", 1);
        
        //------------------------------------------------------------------------------------
        /*You must keep statements pre-given in this function.
       Your task is to insert statements here, just after this comment,
       to complete the question in the exam paper.*/
        addToHead(x);

        //------------------------------------------------------------------------------------
        
        this.displayAll();        
    }

//==================================================================
    void f3(){
        this.clear();
        String[] a = {"C", "D", "E", "F", "I"};
        int[] b =    {9,    6,   3,   2,   6};
        int n = a.length;
        for (int i = 0; i < n; i++) {
            addLast(a[i], b[i]);
        }
        this.displayAll();
        
        int x = 5;
        //------------------------------------------------------------------------------------
        /*You must keep statements pre-given in this function.
       Your task is to insert statements here, just after this comment,
       to complete the question in the exam paper.*/
        Node temp = head;
        while(temp != null){
            if(temp.next != null && temp.next.info.price < x){
                Node next = temp.next.next;
                temp.next = next; 
            }
            temp = temp.next;
        }
        
        //------------------------------------------------------------------------------------
        
        this.displayAll();        
    }

//==================================================================
    void f4() {
        this.clear();
        String[] a = {"C", "D", "E", "F", "I", "J"};
        int[] b =    {9,    6,   5,   13,   2,  1};
        int n = a.length;
        for (int i = 0; i < n; i++) {
            addLast(a[i], b[i]);
        }
        this.displayAll();
        //------------------------------------------------------------------------------------
        /*You must keep statements pre-given in this function.
       Your task is to insert statements here, just after this comment,
       to complete the question in the exam paper.*/  
        Node current = head, index = null;  
        int temp;          
        if(head == null){  
            return;  
        }  
        else{  
            while(current != null) {  
                index = current.next;                  
                while(index != null) {  
                    if(current.info.price > index.info.price ) {  
                        temp = current.info.price ;  
                        current.info.price  = index.info.price ;  
                        index.info.price  = temp;  
                    }  
                    index = index.next;  
                }  
                current = current.next;  
            }      
        }
        //------------------------------------------------------------------------------------
        this.displayAll();        
    }
    void addToTail(String owner, int price){
        Car c = new Car(owner, price);
        Node n = new Node(c);
        if(isEmpty()) head = tail = n;
        else {
            tail.next = n;
            tail = n;
        }
    }
    void addToHead(Car c){
        Node n = new Node(c);
        if(isEmpty()) head = tail = n;
        else{
            n.next = head;
            head = n;
        }
    }
}

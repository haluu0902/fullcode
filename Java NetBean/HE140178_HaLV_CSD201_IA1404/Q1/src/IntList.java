
class IntList {
    Node head, tail;

    IntList() {
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
            System.out.print(p.info + " , "); 
            p = p.next;
        }
        System.out.println("");
    }
    
    void addToTail(int x){
        Node n = new Node(x);
        if(isEmpty()) head = tail = n;
        else {
            tail.next = n;
            tail = n;
        }
    }
//===========================================================================
//(2)===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
//===========================================================================
         
    void addToHead(int x){
        Node n = new Node(x);
        if(isEmpty()) head = tail = n;
        else{
            n.next = head;
            head = n;
        }
    }    
    
    int min(){
        Node p = head;
        int min = head.info;
        while(p != null){
            if(p.info < min && p.info > 0) min = p.info;
            p = p.next;
        }
        return min;
    }
    
    void dele2thPos() {
        int position = 2;
        Node temp = head;
        for (int i=0; temp!=null && i<position-1; i++) 
            temp = temp.next;  
        Node next = temp.next.next;
        temp.next = next; 
    }
    
    boolean search(int x){  
        Node p = head;
        while(p != null && p.info != x) {
            p = p.next;
        }
        if(p == null){
            System.out.println("NOT Found");
            return false;
        }
        else{
            System.out.println("Found");
            return true;
        }
    }
    
    void sortPositive(){
        Node current = head, index = null;  
        int temp;          
        if(head == null){  
            return;  
        }  
        else{  
            while(current != null) { 
                index = current.next;                  
                while(index != null) {  
                    if(current.info > index.info && index.info > 0) { 
                        temp = current.info;  
                        current.info = index.info;  
                        index.info = temp;  
                    }  
                    index = index.next;  
                }  
                current = current.next;  
            }      
        }
    }
    
    int count(){
        Node n = head;
        int count = 0;
        while(n != null){
            if(n.info > 0)
                count += 1;
            n = n.next;
        }
        return count;
    }
}

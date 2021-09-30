/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public class MyLinkedList {
    Node head, tail;
    int count = 0,sum = 0;
    public MyLinkedList(){
        head = tail = null;
    }
    public boolean isEmty(){
        return head == null;
    }
    public void add(int x){
        Node n = new Node(x);
        if(isEmty()) head = tail = n;
        else{
            tail.next = n;
            tail = n;
        }
    }
    public void traverse(){
        Node n = head; 
        Node m = head.next;
        while(n != null){
            if(m != null){
                System.out.print(n.value+", ");
                m = m.next;
            }
            else System.out.print(n.value);
            n = n.next;
        }
        System.out.println();
    }
    public int sum(){
        Node n = head;
        while(n != null){
            sum += n.value;
            n = n.next;
        }
        System.out.println("sum: " + sum);
        return sum;
    }
    public void sort() {  
        Node current = head, index = null;  
        int temp;          
        if(head == null){  
            return;  
        }  
        else{  
            while(current != null) {  
                index = current.next;                  
                while(index != null) {  
                    if(current.value > index.value) {  
                        temp = current.value;  
                        current.value = index.value;  
                        index.value = temp;  
                    }  
                    index = index.next;  
                }  
                current = current.next;  
            }      
        }
        traverse();
    }
    int count() {
        Node n = head; 
        while(n != null){
            count += 1;
            n = n.next;
        }
        System.out.println("count: " + count);
        return count;
    }
    public int dequeue(){
        int x=0;
        if(isEmty()) return x;
        x = head.value;
        head = head.next;
        return x;
    }
    public Node search(int x){
        Node p = head;
        int countS = 0;
        while(p != null && p.value != x) {
            p = p.next;
            countS += 1;
        }
        if(p == null) System.out.println("Not found");
        else System.out.println("Found at the " + countS + "-th position");
        return p;
    }
    public int avg(){
        Node n = head;
        int countA=0;
        int sumA = 0;
        while(n != null){
            countA += 1;
            sumA += n.value;
            n = n.next;
        }
        System.out.println("count: " + countA);
        System.out.println("avg: " + sumA/countA);
        return sumA/countA;
    }
    public int max(){
        Node p = head;
        int max = head.value;
        while(p != null){
            if(p.value > max) max = p.value;
            p = p.next;
        }
        System.out.println(max);
        return max;
    }
}

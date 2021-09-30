/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public class LinkedQueue {
    Node head, tail;
    public LinkedQueue(){
        head = tail = null;
    }
    public boolean isEmty(){
        return head == null;
    }
    public void enqueue(Object x){
        Node n = new Node(x);
        if(isEmty()) head = tail = n;
        else{
            tail.next = n;
            tail = n;
        }
    }
    public Object dequeue(){
        if(isEmty()) return null;
        Object x = head.value;
        head = head.next;
        return x;
    }
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public class MyList {
    Node head, tail;

    public MyList() {
    }

    public void addLast(int x){
        Node n = new Node(x);
        if(head == null) {
            head = n;
            tail = n;
        }
        else{
            tail.next = n;
            tail = n;
        }
    }
    public void traverse(){
        Node tem = head;
        System.out.println("--------------");
        while(tem != null){
            System.out.println(tem.value);
            tem = tem.next;
            
        }
    }
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public class Main {
    public static void main(String[] args) {
        MyLinkedList a = new MyLinkedList();
        a.add(5);
        a.add(7);
        a.add(2); 
        a.add(8); 
        a.add(3);
        a.traverse(); // 5, 7, 2, 8, 3
        a.search(1); // Not found
        a.search(8); // Found at the 3-th position.
        a.max(); // 8;
        a.sum(); // sum: 25
        a.avg(); // avg: 5
        a.count(); // count: 5
        a.sort(); // 2, 3, 5, 7, 8
    }
}

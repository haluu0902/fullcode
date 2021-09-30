/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package assignment3;

import java.util.Scanner;

/**
 *
 * @author LENOVO
 */
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BSTree h = new BSTree();
        int[] a = {12, 7, 1, 3, 2, 5, 10, 8, 6, 9};
        for(int i =0;i<a.length;i++){
            h.insert(a[i]);
        }
//        System.out.println("Search: ");
//        System.out.println(h.search(h.root, 2));
        System.out.println("pre-order:");
        h.preOrder(h.root);
        System.out.println("");
        System.out.println("in-order:");
        h.inOrder(h.root);
        System.out.println("");
        System.out.println("post-order:");
        h.postOrder(h.root);
        System.out.println("");
        System.out.println("Count: " + h.count(h.root));
        System.out.println("Delete:");
        h.delete(sc.nextInt());
        System.out.println("After delete:");
        h.postOrder(h.root);
        System.out.println("");
        System.out.print("Min: ");
        h.minVlaue(h.root);
        System.out.print("Max: ");
        h.maxVlaue(h.root);
        System.out.println("Sum: " + h.sum(h.root));
        System.out.println("Avg: " + h.avg(h.root));
        System.out.println("Height: " + h.height(h.root));
    }
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public class dmBinTree {
    public static void main(String[] args) {
        BinTree tree = new BinTree();   
        tree.inOrder(); 
        System.out.println("\n");
        tree.breadthTraverse();
    }    
}

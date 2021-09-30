/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public class test {
    public static void main(String[] args) {
        System.out.println(fun(7));
    }
    public static void fen(int n) {
        if (n > 1){
        fen(n);
        fen(n);
        }
        System.out.println("*");
    }
    public static int fun(int n){
        if(n<=0) return 1;
        return(3*fun(n-3));
    }
}

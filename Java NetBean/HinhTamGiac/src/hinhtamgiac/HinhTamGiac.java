/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hinhtamgiac;

import java.util.Scanner;

/**
 *
 * @author LENOVO
 */
public class HinhTamGiac {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Tritangle htg = new Tritangle();
        int x,y,z;
        float t;
        System.out.print("Input first edge: ");
        x=sc.nextInt();
        htg.setA(x);
        System.out.print("Input second edge: ");
        y=sc.nextInt();
        htg.setB(y);
        System.out.print("Input third edge: ");
        z=sc.nextInt();
        htg.setC(z);
        System.out.print("Is a Triangle: ");
        if(htg.isATriangle()){
            System.out.println("True");
        }
        else{
            System.out.println("False");
            System.exit(0);
        }
        int primeter = htg.computePrimeter();
        float area = htg.computeArea();
        System.out.println("Triangular circumference: " + primeter);
        System.out.println("Triangle area: " + area);
    }
    
}

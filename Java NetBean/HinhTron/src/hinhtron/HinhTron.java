/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hinhtron;

import java.util.Scanner;

/**
 *
 * @author LENOVO
 */
public class HinhTron {

    public static void main(String[] args) {
        float r;
        Circle hT = new Circle();
        Scanner sc = new Scanner(System.in);
        System.out.print("Input radius r = ");
        r=sc.nextFloat();
        hT.setR(r);        
        float primeter = hT.computePrimeter();
        float area = hT.computeArea();
        System.out.println("Diameter of a circle: " + primeter);
        System.out.println("Circle area: " + area);
    }
}



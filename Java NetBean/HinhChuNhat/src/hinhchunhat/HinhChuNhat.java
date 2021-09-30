/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hinhchunhat;

import java.util.Scanner;

/**
 *
 * @author LENOVO
 */
public class HinhChuNhat {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Rectangle hcn = new Rectangle();
        int x, y;
        System.out.print("Input length of the rectangle: ");
        x = sc.nextInt();
        hcn.setD(x);
        System.out.print("Input width of the rectangle ");
        y = sc.nextInt();
        hcn.setR(y);
        int primeter = hcn.computePrimeter();
        int area = hcn.computeArea();
        System.out.println("Perimeter of a rectangle: " + primeter);
        System.out.println("Rectangular area: " + area);
    }

}

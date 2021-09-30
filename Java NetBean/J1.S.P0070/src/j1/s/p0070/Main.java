/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package j1.s.p0070;

import java.util.Scanner;
import java.util.ResourceBundle;
import java.util.Random;

/**
 *
 * @author PH
 */
public class Main {
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        Ebank e = new Ebank();
        boolean status = true;
        String choice;
        while(status){
            System.out.println("-------Login Program-------");
            System.out.println("1. Vietnamese");
            System.out.println("2. English");
            System.out.println("3. Exit");
            System.out.print("Please choice one option: ");
            choice = sc.nextLine();
            switch(choice){
                case "1":{
                    ResourceBundle laguage = ResourceBundle.getBundle("language_vi_VN");
                    e.Login(laguage);
                    break;
                }                    
                case "2" :{
                    break;
                }
                case "3" :{
                    status = false;
                    break;
                }    
            }
        }
    }
}

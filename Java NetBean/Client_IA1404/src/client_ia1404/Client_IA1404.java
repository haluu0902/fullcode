/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package client_ia1404;

import java.net.Socket;
import java.util.Scanner;

/**
 *
 * @author PH
 */
public class Client_IA1404 {
    Socket sc;
    public Client_IA1404(){        
        try {
            sc = new Socket("localhost",123456);
        } catch (Exception e) {
        }
    }
    Thread t1,t2;
    private void initThread(){
        Scanner sc = new Scanner(System.in);
        t1 = new Thread(){
            @Override
            public void run() {
                while(true){
                    System.out.println("Input id: ");
                    String id = sc.nextLine();
                    System.out.println("Input id: ");
                    String name = sc.nextLine();
                    System.out.println("Input id: ");
                    int age = Integer.parseInt(sc.nextLine());
                    Student st = new Student(id, name, age);
                }
            }
            
        };
        t2 = new Thread(){
            @Override
            public void run() {
                try {
                    
                } catch (Exception e) {
                }
            }
            
        };
    }
    public static void main(String[] args) {
        new Client_IA1404();
    }
}

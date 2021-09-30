/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package server_ia1404;

import java.net.ServerSocket;
import java.net.Socket;

/**
 *
 * @author PH
 */
public class Server_IA1404 {
    ServerSocket ss;
    Socket sc;
    public Server_IA1404(){
        try {
            ss = new ServerSocket(123456);
            System.out.println("Da san sang");
            sc = ss.accept();
            System.out.println("Khach da den");
        } catch (Exception e) {
        }
    }
    public static void main(String[] args) {
        new Server_IA1404();
    }
}

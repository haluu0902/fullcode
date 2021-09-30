 /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package TestConnection;

import context.DBContext;
import java.sql.Connection;

/**
 *
 * @author LENOVO
 */
public class Test {
    Connection con;
    
    public Test(){
        try{
            con = new DBContext().getConnection();
            System.out.println("Ket Noi Thanh Cong");
        }catch(Exception e){
            System.out.println("Ket Noi That Bai "+e.getMessage());
        }
    }
    public static void main(String[] args) {
        new Test();
    }
}

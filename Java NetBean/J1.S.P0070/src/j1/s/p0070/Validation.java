/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package j1.s.p0070;
import java.util.ResourceBundle;
import java.util.Scanner;
/**
 *
 * @author PH
 */
public class Validation {
    private final Scanner sc = new Scanner(System.in);
    private final String ACC_NUM = "^[0-9]{10}$";
    private final String ACC_PW = "^(?=.*[0-9])(?=.*[a-zA-Z]).{8,31}$";
    public String CheckAccNum(ResourceBundle bundle){
        String accNum;
        while(true){
            System.out.print(bundle.getString("account"));
            accNum = sc.nextLine();
            if(accNum.matches(ACC_NUM))
                break;
            else
                System.err.println(bundle.getString("wrong.account"));
        }
        return accNum; 
    }
    public String CheckAccPw(ResourceBundle bundle){
        String accPw;
        while(true){
            System.out.print(bundle.getString("account"));
            accPw = sc.nextLine();
            if(accPw.matches(ACC_PW))
                break;
            else
                System.err.println(bundle.getString("wrong.password"));
        }
        return accPw; 
    }
}

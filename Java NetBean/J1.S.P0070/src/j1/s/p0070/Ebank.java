/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package j1.s.p0070;

import java.util.ResourceBundle;
import java.util.Scanner;
import java.nio.charset.Charset;
/**
 *
 * @author PH
 */
public class Ebank {
    
    public Validation val = new Validation();
    public static Scanner sc = new Scanner(System.in);
    int accNum;
    public void Login(ResourceBundle bundle){
        String accNum = val.CheckAccNum(bundle);
        String accPw;
    }
    public String genCaptcha(int numSize){
        String captcha;
        byte []array = new byte[256];
        String randomString;
        for(int count=0 ; count < 5 ; count++){
            randomString = ra
        }
        return captcha;
    }
}

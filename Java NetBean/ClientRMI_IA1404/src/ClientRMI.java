
import java.net.MalformedURLException;
import java.rmi.AlreadyBoundException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.registry.LocateRegistry;
import java.util.logging.Level;
import java.util.logging.Logger;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public class ClientRMI {
    public static void main(String[] args) {
        try {
            Calculator cal = (Calculator)Naming.lookup("rmi://localhost:22334/Cal");
            int a = 10, b= 20;
            System.out.println("Ket qua cua RMI: " + cal.Add(a, b));
        } catch (NotBoundException ex) {
            Logger.getLogger(ClientRMI.class.getName()).log(Level.SEVERE, null, ex);
        } catch (MalformedURLException ex){
            Logger.getLogger(ClientRMI.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception e){
            
        }
    }
}

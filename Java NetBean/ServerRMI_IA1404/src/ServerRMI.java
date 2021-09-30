
import java.net.MalformedURLException;
import java.rmi.AlreadyBoundException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
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
public class ServerRMI extends UnicastRemoteObject implements Calculator{
    
    public ServerRMI() throws RemoteException{
        
    }

    @Override
    public int Add(int a, int b) throws RemoteException {
        return a+b;
    }

    @Override
    public int Sub(int a, int b) throws RemoteException {
        return a-b;
    }    
    
    public static void main(String[] args) {
        try {
            ServerRMI server = new ServerRMI();
            LocateRegistry.createRegistry(22334);
            Naming.bind("rmi://localhost:22334/Cal", server);
            System.out.println("Server san sang");
        } catch (AlreadyBoundException ex) {
            Logger.getLogger(ServerRMI.class.getName()).log(Level.SEVERE, null, ex);
        } catch (MalformedURLException ex){
            Logger.getLogger(ServerRMI.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception e){
            
        }
        
    }
}

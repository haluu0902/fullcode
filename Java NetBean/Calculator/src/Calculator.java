
import java.rmi.Remote;
import java.rmi.RemoteException;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public interface Calculator extends Remote{
    public int Add(int a, int b) throws RemoteException;
    public int Sub(int a, int b) throws RemoteException;
}

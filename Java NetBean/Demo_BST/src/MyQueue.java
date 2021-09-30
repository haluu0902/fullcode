/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
import java.util.ArrayList;
class MyQueue{
    ArrayList al = new ArrayList();
    public boolean isEmpty(){   return al.isEmpty();    }
    public void enQueue(Object x){  al.add(x);          }
    public Object deQueue(){    return(al.remove(0));   }
}

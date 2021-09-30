/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package csd201_1;

/**
 *
 * @author PH
 */
public class CSD201_1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int []num = {100,111,123,23,1,4,6,8,3,5};
        int max=num[0];
        int max2=num[0];
        for (int numCont : num){
            if(numCont > max){
                if(max != max2)
                    max2 = max;
                max = numCont;
            }
        }
        System.out.println("Max 2 = " + max2);
    }    
}

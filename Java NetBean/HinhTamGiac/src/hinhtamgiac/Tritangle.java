/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hinhtamgiac;

/**
 *
 * @author LENOVO
 */
public class Tritangle {
    private int a,b,c,p;

    public Tritangle() {
    }

    public Tritangle(int a, int b, int c, float h) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public int getA() {
        return a;
    }

    public int getB() {
        return b;
    }

    public int getC() {
        return c;
    }


    public void setA(int a) {
        this.a = a;
    }

    public void setB(int b) {
        this.b = b;
    }

    public void setC(int c) {
        this.c = c;
    }

        
    public int computePrimeter(){
        return a+b+c;
    }
    public float computeArea(){
        p = (a + b + c) / 2;
        return (float)(Math.sqrt(p*(p-a)*(p-b)*(p-c)));
    }
    public boolean isATriangle(){
        boolean status = true;
        if(a+b<=c || a+c<=b || b+c<=a)
            status = false;
        return status;
    }
}

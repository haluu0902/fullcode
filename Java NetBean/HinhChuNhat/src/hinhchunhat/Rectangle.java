/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hinhchunhat;

/**
 *
 * @author LENOVO
 */
public class Rectangle {

    private int d;
    private int r;

    public Rectangle() {
    }

    public Rectangle(int d, int r) {
        this.d = d;
        this.r = r;
    }

    public int getD() {
        return d;
    }

    public int getR() {
        return r;
    }

    public void setD(int d) {
        this.d = d;
    }

    public void setR(int r) {
        this.r = r;
    }
    public int computePrimeter(){
        return (d + r) * 2;
    }
    public int computeArea(){
        return d*r;
    }
}

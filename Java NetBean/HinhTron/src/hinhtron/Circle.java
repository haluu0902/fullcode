/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hinhtron;

/**
 *
 * @author LENOVO
 */
class Circle {

    private final float PI = 3.14f;
    private float r;

    public Circle() {
    }

    public Circle(float r) {
        this.r = r;
    }

    public float getR() {
        return r;
    }

    public void setR(float r) {
        this.r = r;
    }

    public float computePrimeter() {
        return 2 * PI * r;
    }

    public float computeArea() {
        return PI * r * r;
    }
}

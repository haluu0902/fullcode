/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */

import java.io.Serializable;
public class Student implements Serializable{
    String ID;
    String name;
    int age;

    public Student(String ID, String name, int age) {
        this.ID = ID;
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Student{" + "ID=" + ID + ", name=" + name + ", age=" + age + '}';
    }
    
    
}

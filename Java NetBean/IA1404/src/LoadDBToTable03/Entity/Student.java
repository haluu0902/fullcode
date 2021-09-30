/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LoadDBToTable03.Entity;

/**
 *
 * @author LENOVO
 */
public class Student {
    private String ID;
    private String name;
    private boolean gender;
    private String DepartID;
    private float GPA;
    private String Address;
    private boolean Update = false;

    public boolean isUpdate() {
        return Update;
    }
    

    public void setUpdate(boolean Update) {
        this.Update = Update;
    }

    public Student(String ID, String name, boolean gender, String DepartID, float GPA, String Address) {
        this.ID = ID;
        this.name = name;
        this.gender = gender;
        this.DepartID = DepartID;
        this.GPA = GPA;
        this.Address = Address;
    }

    public Student() {
    }

 

    public void setID(String ID) {
        this.ID = ID;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setGender(boolean gender) {
        this.gender = gender;
    }

    public void setDepartID(String DepartID) {
        this.DepartID = DepartID;
    }

    public void setGPA(float GPA) {
        this.GPA = GPA;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public String getID() {
        return ID;
    }

    public String getName() {
        return name;
    }

    public boolean isGender() {
        return gender;
    }

    public String getDepartID() {
        return DepartID;
    }

    public float getGPA() {
        return GPA;
    }

    public String getAddress() {
        return Address;
    }
    
    
}

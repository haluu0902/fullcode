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
public class Department {
    private String DepartID;
    private String DepartName;
    private String DepartInfor;

    public Department(String DepartID, String DepartName, String DepartInfor) {
        this.DepartID = DepartID;
        this.DepartName = DepartName;
        this.DepartInfor = DepartInfor;
    }

    public Department() {
    }

    public String getDepartID() {
        return DepartID;
    }

    public String getDepartName() {
        return DepartName;
    }

    public String getDepartInfor() {
        return DepartInfor;
    }

    public void setDepartID(String DepartID) {
        this.DepartID = DepartID;
    }

    public void setDepartName(String DepartName) {
        this.DepartName = DepartName;
    }

    public void setDepartInfor(String DepartInfor) {
        this.DepartInfor = DepartInfor;
    }
    
}

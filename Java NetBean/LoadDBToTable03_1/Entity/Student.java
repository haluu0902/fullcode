
package LoadDBToTable03.Entity;

/**
 *
 * @author LTTH
 */
public class Student {
    private String ID;
    private String name;
    private boolean gender;
    private String DepartID;
    private float GPA;
    private String Address;
    private boolean Update = false;

    public Student() {
    }

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

    public String getID() {
        return ID;
    }

    public void setID(String ID) {
        this.ID = ID;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean isGender() {
        return gender;
    }

    public void setGender(boolean gender) {
        this.gender = gender;
    }

    public String getDepartID() {
        return DepartID;
    }

    public void setDepartID(String DepartID) {
        this.DepartID = DepartID;
    }

    public float getGPA() {
        return GPA;
    }

    public void setGPA(float GPA) {
        this.GPA = GPA;
    }

    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    @Override
    public String toString() {
        return ID + ", " + name + ", " + gender + ", " + DepartID + ", " + GPA + ", " + Address;
    }
                
}

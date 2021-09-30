
package LoadDBToTable03.Entity;

/**
 *
 * @author LTTH
 */
public class Department {
    private String DepartID;
    private String DepartName;
    private String DepartInfo;

    public Department(String DepartID, String DepartName, String DepartInfo) {
        this.DepartID = DepartID;
        this.DepartName = DepartName;
        this.DepartInfo = DepartInfo;
    }

    public String getDepartID() {
        return DepartID;
    }

    public void setDepartID(String DepartID) {
        this.DepartID = DepartID;
    }

    public String getDepartName() {
        return DepartName;
    }

    public void setDepartName(String DepartName) {
        this.DepartName = DepartName;
    }

    public String getDepartInfo() {
        return DepartInfo;
    }

    public void setDepartInfor(String DepartInfo) {
        this.DepartInfo = DepartInfo;
    }
    
    
}

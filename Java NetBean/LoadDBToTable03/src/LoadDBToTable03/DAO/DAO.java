package LoadDBToTable03.DAO;
import LoadDBToTable03.Entity.Department;
import LoadDBToTable03.Entity.Student;
import context.DBContext;
import java.sql.*;
import java.util.*;
import java.util.HashSet;
import java.util.List;
import java.util.Vector;
/**
 *
 * @author LENOVO
 */
public class DAO {
    private Connection con;
    private HashMap<String, Student> student;
    public Connection getCon() {
        return con;
    }
    public void setCon(Connection con) {
        this.con = con;
    }
    public HashMap<String, Student> getStudent() {
        return student;
    }
    public void setStudent(HashMap<String, Student> student) {
        this.student = student;
    }
    public DAO(){
        initConnection();
        String sql = "select * from StudentInfo";
        getListStudent(sql);
//        getDepart();
    }
    private void initConnection() {
        try{
            con = new DBContext().getConnection();
        }catch(Exception e){
        }
    }    
    HashSet<String> hs;
    public void getListStudent(String sql){
//        hs = new HashSet<String>();
//        student = new Vector<Student>(); // Vecto co dong bo, ArrayList thi khong
        student = new HashMap<String, Student>();
        try{
            PreparedStatement ps = con.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                hs.add(rs.getString(1));
                student.put(rs.getString(1), new Student(
                        rs.getString(1), rs.getString(2), rs.getBoolean(3),
                        rs.getString(4), Float.parseFloat(rs.getString(5)),
                        rs.getString(6)
                ));
            }
        }catch(Exception e){
        }
    }
    public void putListToDB(){
//        Vector <Student> vec = new Vector<Student>;
//        Set key = student.keySet();
        HashMap<String, Student> temp = new HashMap<String, Student>();
        for (Map.Entry<String, Student> entry : student.entrySet()) {
            String key = entry.getKey();
            Student value = entry.getValue();
            temp.put(key, value);
        }
        HashSet <String> tempID = new HashSet<String>();
        for (Map.Entry<String, Student> entry : temp.entrySet()) {
            String key = entry.getKey();
            Student value = entry.getValue();
            if(hs.contains(key)){
                if(temp.get(key).isUpdate()){
                    String sql = "Update StudenInfo set Name = '"+
                            value.getName()+"', gender = "+
                            (value.isGender()?1:0)+", DepartId = '"+
                            value.getDepartID()+"', GPA = "+
                            value.getGPA()+"', Address = "+
                            value.getAddress()+"' where Id = '"+
                            value.getID()+"'";
                    //Update
                    myQueue(sql);
                }
                tempID.add(key);
//                temp.remove(key);
//                hs.remove(key);
            }
        }
        for(Iterator<String> iterator = hs.iterator();iterator.hasNext();){
            String next = iterator.next();
            if(!tempID.contains(next)){
                //Delete database with ID= next
            }
        }
        for (Map.Entry<String, Student> entry : temp.entrySet()) {
            String key = entry.getKey();
            Student value = entry.getValue();
            if(!tempID.contains(key)){
                //Insert voi ID=key
            }
        }
        hs = new HashSet<String>(); // Luu key cua database
        for (Map.Entry<String, Student> entry : student.entrySet()) {
            String key = entry.getKey();
            Student value = entry.getValue();
            hs.add(key);
        }

        
//        for(Iterator iterator = key.iterator();iterator.hasNext();){
//            String next = iterator.next()+"";
//            if(hs.contains(next)){
//                //Update
//            }
//        }
        }
//        for(int i=0;i<student.size();i++){
//            Student st = student.get(i);
//            if(hs.contains(st.getID())){
//                // Update
//                hs.remove(i);
//                student.remove(i);
//                i--;
//            }
//        }
//    for(int i=0;i<hs.size();i++){
//        // Delete (hs.get(i))
//    }  
//     for(int i=0;i<student.size();i++){
//        // Insert
//        String sql = "Insert into studentInfo values ("+student.get(i)+")";
//    }  
//    }
    void myQueue(String sql){
        try{
            PreparedStatement ps = con.prepareStatement(sql);
            ps.execute();
        }catch(Exception e){
        }
    } 
    private HashMap<String, Department> HmDepart;
    private HashMap<String, String> reverseHm;
    public HashMap<String, Department> getHmDepart() {
        return HmDepart;
    }
    public HashMap<String, String> getReverseHm() {
        return reverseHm;
    }
    public void GetDepart(){
        String sql="select * from DepartInfo";
        HmDepart= new HashMap<String, Department>();
        reverseHm= new HashMap<String, String>();
        try{
            PreparedStatement ps=con.prepareStatement(sql);
            ResultSet rs=ps.executeQuery();
            while(rs.next()){
                HmDepart.put(rs.getString(1), new Department(
                        rs.getString(1),  rs.getString(2),  rs.getString(3)
                ));
                reverseHm.put(rs.getString(2), rs.getString(1));
            }
        }catch(Exception e){
        }
    }
}
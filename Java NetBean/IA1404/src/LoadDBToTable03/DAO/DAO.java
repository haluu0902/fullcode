package LoadDBToTable03.DAO;
import LoadDBToTable03.Entity.Department;
import LoadDBToTable03.Entity.Student;
import context.DBContext;
import java.awt.RenderingHints.Key;
import java.sql.*;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Vector;
/**
 *
 * @author LTTH
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
    public HashMap<String,Student> getStudent() {
        return student;
    }
    public void setStudent(HashMap<String,Student> student) {
        this.student = student;
    }
    public DAO(){
        initConnection();
    }
    private void initConnection() {
        try{
            con = new DBContext().getConnection();
        }catch(Exception e){
        }
    }
    
    HashSet<String> hs;
    public void getListStudent(String sql){
        hs = new HashSet<String>();
        //student = new Vector<Student>(); // Vecto co dong bo, ArrayList thi khong
        student = new HashMap<String, Student>();
        try{
            PreparedStatement ps = con.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                hs.add(rs.getString(1));
                student.put(rs.getString(1),new Student(
                        rs.getString(1), rs.getString(2), rs.getBoolean(3),
                        rs.getString(4), Float.parseFloat(rs.getString(5)),
                        rs.getString(6)
                ));
            }
        }catch(Exception e){
        }
    }
    void putListToDB(){
        HashMap<String, Student> temp = new HashMap<String, Student>();
        for (Map.Entry<String, Student> entry : temp.entrySet()) {
            String key = entry.getKey();
            Student value = entry.getValue();
            temp.put(key, value);
            
        }
        student = new HashMap<String, Student>();
        for(Map.Entry<String, Student> entry : student.entrySet()){
            String key = entry.getKey();
            Student value = entry.getValue();
            if(hs.contains(key)){
                if(temp.get(key).isUpdate()){
                    
                }
                temp.remove(key);
                hs.remove(key);
            }
        }
        for(Iterator<String> iterator = hs.iterator(); iterator.hasNext();){
            String next = iterator.next();
        }
        for(Map.Entry<String, Student> entry : temp.entrySet()){
            String key = entry.getKey();
            Student value = entry.getValue();
        }
        hs = new HashSet<>();
        for(Map.Entry<String, Student> entry : student.entrySet()){
            String key = entry.getKey();
            Student value = entry.getValue();
            hs.add(key);
        }
    }
////        Vector <Student> vec = new Vector<Student>;
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
        String sql = "Select * from DepartInfor";
        HmDepart = new HashMap<String, Department>();
        reverseHm = new HashMap<String, String>();
        try{
            PreparedStatement ps = con.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                HmDepart.put(rs.getString(1)), new Department(
                        rs.getString(1),rs.getString(2),rs.getString(3)
                ));
                reverseHm.put(rs.getString(2), rs.getString(1));
            }
        }
        catch(Exception e){
            
        }
    }
}
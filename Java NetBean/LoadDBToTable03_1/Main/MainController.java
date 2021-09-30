
package LoadDBToTable03.Main;
import java.sql.*;
import java.util.*;
import LoadDBToTable03.DAO.DAO;
import LoadDBToTable03.Entity.*;
import LoadDBToTable03.View.LoadTable;
import context.DBContext;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.table.DefaultTableModel;
/**
 *
 * @author LTTH
 */
public class MainController {
    LoadTable f1;
    DAO dao;

    public MainController(LoadTable f1) {
        this.f1 = f1;
        dao = new DAO();
        String sql = "Select s.ID, s.Name, s.Gender, d.Department, s.GPA, s.Address from StudentInfo s, DepartInfo d where s.DepartID=d.DepartID";
        dao.getListStudent(sql);
        dao.GetDepart();
    }
    public void control(){
        f1.setVisible(true);
        xulyLoad();
        xulyUpdate();
    }
    private void xulyUpdate(){
        f1.getBtnUpdate().addActionListener((evt)->{
          Student st = new Student(f1.getTxtID().getText(),
                  f1.getTxtName().getText(),
                  f1.getChkGender().isSelected(),
                  "SE",
                  Float.parseFloat(f1.getTxtGPA().getText()),
                  f1.getTxtAddress().getText());
          st.setUpdate(true);
          dao.getStudent().put(f1.getTxtID().getText(),st);
          load();
    });
    }
    String [] title = {"Id", "Name", "Gender", "DepartName", "GPA", "Address"};
    DefaultTableModel dftm = new DefaultTableModel();
    
    private void xulyLoad(){
        f1.getBtnLoad().addActionListener((evt)->{
            load();
        });
    }
    
    private void load(){
        dftm.setColumnIdentifiers(title);
        dftm.setRowCount(0);
        for (Map.Entry<String, Student> entry : dao.getStudent().entrySet()) {
            String key = entry.getKey();
            Student value = entry.getValue();
            dftm.addRow(putStudent(value));
        }
        f1.getTblDisplay().setModel(dftm);
    }
//    private void xulyLoad(){
//        f1.getBtnLoad().addActionListener(new ActionListener() {
//            @Override
//            public void actionPerformed(ActionEvent e) {
//                        dftm.setColumnIdentifiers(title);
//        dftm.setRowCount(0);
//        for (Map.Entry<String, Student> entry : dao.getStudent().entrySet()) {
//            String key = entry.getKey();
//            Student value = entry.getValue();
//            dftm.addRow(putStudent(value));
//            
//        }
//        f1.getTblDisplay().setModel(dftm);
//            }
//       });
//        dftm.setColumnIdentifiers(title);
//        dftm.setRowCount(0);
//        for (Map.Entry<String, Student> entry : dao.getStudent().entrySet()) {
//            String key = entry.getKey();
//            Student value = entry.getValue();
//            dftm.addRow(putStudent(value));
//            
//        }
//        f1.getTblDisplay().setModel(dftm);
    
    private Vector putStudent(Student s){
        Vector v = new Vector();
        v.add(s.getID());
        v.add(s.getName());
        v.add(s.isGender());
        v.add(s.getDepartID());
        v.add(s.getGPA());
        v.add(s.getAddress());
        return v;
    }
    public static void main(String[] args) {
        new MainController(new LoadTable()).control();
    }
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LoadDBToTable03.Main;
import java.sql.*;
import java.util.*;
import LoadDBToTable03.DAO.DAO;
import LoadDBToTable03.DAO.DAO;
import LoadDBToTable03.Entity.*;
import LoadDBToTable03.View.LoadTable;
import context.DBContext;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;
import javax.swing.Timer;
/**
 *
 * @author LENOVO
 */
public class MainController {
    LoadTable f1;
    DAO dao;
    public MainController(LoadTable f1) {
        this.f1 = f1;
        dao = new DAO();
        String sql = "Select s.ID, s.Name, s.Gender, d.DepartID, s.GPA, s.Address from StudentInfor s, DepartInfor d where s.DepartID=d.DepartID";
        dao.getListStudent(sql);
        dao.GetDepart();
    }
    public void control(){
        f1.setVisible(true);
        xulyLoad();
        xulyUpdate();
        xulyDelete();
        initLoadDepartName();
        xulyCareUpdateID();
        xulybtnDongBo();
    }
    
    Timer t;
    private void autoDongBo(){
        t = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dao.putListToDB();
            }
        });
        t.start();
    }
    private void xulybtnDongBo(){
        f1.getBtnDongBo().addActionListener((evt) ->{
            int ans = JOptionPane.showConfirmDialog(f1, "Do you want Synchronize DB");
            if(ans == 0){
                dao.putListToDB();
                System.out.println("Da dong bo xong du lieu");
            }                
        });
    }
    private void initLoadDepartName(){
        Vector<String> v = new Vector<String>();
        for (Map.Entry<String, Department> entry : dao.getHmDepart().entrySet()) {
            String key = entry.getKey();
            Department value = entry.getValue();
            v.add(value.getDepartName());
        }
        f1.getCbxDepartName().setModel(new DefaultComboBoxModel<>(v));
    }
    private void xulyUpdate(){
        f1.getBtnUpdate().addActionListener((evt)->{
          Student st = new Student(f1.getTxtID().getText(),
                  f1.getTxtName().getText(),
                  f1.getChkGender().isSelected(),
                //  "SE",
                  dao.getReverseHm().get(f1.getCbxDepartName().getSelectedItem()+""),
                  Float.parseFloat(f1.getTxtGPA().getText()),
                  f1.getTxtAddress().getText());
          st.setUpdate(true);
          dao.getStudent().put(f1.getTxtID().getText(),st);
          load();
    });
    }
    private void xulyCareUpdateID(){
        f1.getTxtID().addCaretListener((evt) ->{
            String id = f1.getTxtID().getText();
            if(id.length()==0){
                f1.getBtnDelete().setEnabled(false);
                f1.getBtnInsert().setEnabled(false);
                f1.getBtnUpdate().setEnabled(false);
            }else{
                if(dao.getStudent().containsKey(id)){
                    f1.getBtnDelete().setEnabled(true);
                    f1.getBtnInsert().setEnabled(false);
                    f1.getBtnUpdate().setEnabled(true);
                }else{
                    f1.getBtnDelete().setEnabled(false);
                    f1.getBtnInsert().setEnabled(true);
                    f1.getBtnUpdate().setEnabled(false);
                }
            }
        });
    }
    private void xulyDelete(){
        f1.getBtnDelete().addActionListener((evt) ->{
            String id = f1.getTxtID().getText();
            int ans = JOptionPane.showConfirmDialog(f1, "Do you want to delete student with id = "+id+"? ", "Delete ID "+id, 0);
            if(ans==0){
                dao.getStudent().remove(id);
                load();
            }
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
    private Vector putStudent(Student s){
        Vector v = new Vector();
        v.add(s.getID());
        v.add(s.getName());
        v.add(s.isGender());
//        v.add(s.getDepartID());
        v.add(dao.getHmDepart().get(s.getDepartID()).getDepartName());
        v.add(s.getGPA());
        v.add(s.getAddress());
        return v;
    }
    public static void main(String[] args) {
        new MainController(new LoadTable()).control();
    }
}
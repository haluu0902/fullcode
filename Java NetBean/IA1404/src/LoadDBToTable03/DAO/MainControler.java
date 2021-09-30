/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LoadDBToTable03.DAO;
import java.sql.*;
import java.util.*;
import LoadDBToTable03.DAO.DAO;
import LoadDBToTable03.Entity.*;
import LoadDBToTable03.View.LoadTable;
import LoadDbtoTable.LoadTable;
import context.DBContext;
import javax.swing.table.DefaultTableModel;
/**
 *
 * @author PH
 */
public class MainControler {
    LoadTable f1;
    DAO dao;
    public MainControler(LoadTable f1){
        this.f1 = f1;
        dao = new DAO();
        String sql = "select s.ID, s.Name, s.Gender, d.Departname, s.GPA, s.Address from StudentInfor s, DepartInfor d";
        dao.getListStudent(sql);
        dao.GetDepart();
    }
    public void control(){
        f1.setVisible(true);
        xulyLoad();
    }
    String[] title ={"ID","Name","Gender","DepartName","GPA","Address"};
    DefaultTableModel dfm = new DefaultTableModel();
    private void xulyLoad(){
        f1.getBtnLoad().addActionListioner((evt))
        dfm.setColumnIdentifiers(title);
        dfm.setRowCount(0);
        for(Map.Entry<String,Student> entry : dao.getStudent().entrySet()){
            String key = entry.getKey();
            Student value = entry.getValue();
            
        }
    }
}

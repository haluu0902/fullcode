package LoadDBToTable02;

import context.DBContext;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Vector;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JOptionPane;
import javax.swing.event.CaretEvent;
import javax.swing.event.CaretListener;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author LTTH
 */

public class MainController {
    LoadToTable f1;

    public MainController(LoadToTable f1) {
        this.f1 = f1;
    }

    public MainController() {    
    }
    
    private void control(){
        f1.setVisible(true);
        initConnection();
        LoadDepartName();    
        xulyId();
        btnLoad();
        xulyInsert();
        xulyUpdate();
        xulyDelete();      
    }
    
    Connection con;
    DefaultTableModel dftm = new DefaultTableModel();
    HashSet<String> hs;
    HashMap<String,String> hm;
    
    private void TableAction(){
        f1.getTblDisplay().getSelectionModel().addListSelectionListener(new ListSelectionListener() {
            @Override
            public void valueChanged(ListSelectionEvent e) {
               int n = f1.getTblDisplay().getSelectedRow();
               if(n>=0){
               f1.getTxtID().setText(f1.getTblDisplay().getValueAt(n, 0)+"");
               f1.getTxtName().setText(f1.getTblDisplay().getValueAt(n, 1)+ "");
               String select =f1.getTblDisplay().getValueAt(n, 2)+ "";
               f1.getChkGender().setSelected(select.equals("true"));
               f1.getCbxDepartName().setSelectedItem(f1.getTblDisplay().getValueAt(n, 3)+ "");
               f1.getTxtGPA().setText(f1.getTblDisplay().getValueAt(n, 4)+ "");
               f1.getTxtAddress().setText(f1.getTblDisplay().getValueAt(n, 5)+ "");
               }               
            }
        });
    }
    
     private void LoadDepartName(){
        String sql = "Select * from DepartInfo";
        Vector vec = new Vector();
        try{
            PreparedStatement ps = con.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            hm=new HashMap<>();
            while(rs.next()){
                vec.add(rs.getString(2));
                hm.put(rs.getString(2),rs.getString(1));
            }
            f1.getCbxDepartName().setModel(new DefaultComboBoxModel<String>(vec));
        }catch(Exception e){
            System.out.println("Co loi: " + e.getMessage());
        }
    }
     
     private void initConnection(){
        try{
            con = new DBContext().getConnection();
            System.out.println("Ket noi thanh cong");
        } catch (Exception e){
            System.out.println("Ket noi that bai: " + e.getMessage());
        }
    }
     
      private void Load(){
        dftm = new DefaultTableModel();
        String[] title={"ID", "Full Name", "Gender", "DepartName", "GPA", "Address"};
        dftm.setColumnIdentifiers(title);
//        String sql = "Select * from StudentInfo";
        String sql = "Select s.ID, s.Name, s.Gender, d.DepartName,s.GPA, s.[Address] from StudentInfo s, Departinfo d where s.DepartID=d.DepartID;";
        dftm.setRowCount(0);
        try{
            PreparedStatement ps = con.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            Vector vec;
            hs = new HashSet<String>();
            while(rs.next()){
                vec = new Vector();
                vec.add(rs.getString(1));
                hs.add(rs.getString(1));
                vec.add(rs.getString("Name"));
                vec.add(rs.getBoolean("Gender"));            
                vec.add(rs.getString(4));
                vec.add(rs.getFloat(5));
                vec.add(rs.getString(6));
                dftm.addRow(vec);
            }
            f1.getTblDisplay().setModel(dftm);
        } catch(Exception e){
            System.out.println("Co loi: " +e.getMessage());
        }
    }
      
      private void btnLoad(){
          f1.getBtnLoad().addActionListener(new ActionListener() {
              @Override
              public void actionPerformed(ActionEvent e) {
                 Load();
                TableAction();
                f1.getBtnLoad().setEnabled(false);
              }
          });          
      }
      
      private void xulyId(){
         f1.getTxtID().addCaretListener(new CaretListener() {
             @Override
             public void caretUpdate(CaretEvent e) {
              if(f1.getTxtID().getText().length()==0){
                    f1.getBtnDelete().setEnabled(false);
                    f1.getBtnInsert().setEnabled(false);
                    f1.getBtnUpdate().setEnabled(false);
                }else{
                if(hs.contains(f1.getTxtID().getText())){
                    f1.getBtnDelete().setEnabled(true);
                    f1.getBtnInsert().setEnabled(false);
                    f1.getBtnUpdate().setEnabled(true);
                }else{
                    f1.getBtnDelete().setEnabled(false);
                    f1.getBtnInsert().setEnabled(true);
                    f1.getBtnUpdate().setEnabled(false);
                }   
                }
             }
         });
    }
      
      private void xulyInsert(){
         f1.getBtnInsert().addActionListener(new ActionListener() {
             @Override
             public void actionPerformed(ActionEvent e) {
                 String sql = "INSERT INTO StudentInfo VALUES (?,?,?,?,?,?)";
        try{
            PreparedStatement ps = con.prepareStatement(sql);
            ps.setString(1, f1.getTxtID().getText());
            ps.setString(2, f1.getTxtName().getText());
            ps.setBoolean(3, f1.getChkGender().isSelected());
            ps.setFloat(5, Float.parseFloat(f1.getTxtGPA().getText()));
            ps.setString(6, f1.getTxtAddress().getText());
            ps.setString(4, hm.get(f1.getCbxDepartName().getSelectedItem()+""));
            ps.execute();
            Load();
            f1.getTxtID().setText("");
        }catch(NumberFormatException | SQLException d){
            System.out.println("Loi gi day: "+d.getMessage());
        }
        Load();
             }
         });
      }
      
      private void xulyUpdate(){
          f1.getBtnUpdate().addActionListener(new ActionListener() {
              @Override
              public void actionPerformed(ActionEvent e) {
                  String sql = "update StudentInfo set Name= ?,Gender=?"+",DepartID=? ,GPA=?,Address=? where ID =?";
        try {
            PreparedStatement ps = con.prepareStatement(sql);
            ps.setString(1,f1.getTxtName().getText());
            ps.setBoolean(2, f1.getChkGender().isSelected());
            ps.setFloat(4, Float.parseFloat(f1.getTxtGPA().getText()));
            ps.setString(3, hm.get(f1.getCbxDepartName().getSelectedItem()+""));
            ps.setString(5, f1.getTxtAddress().getText());
            ps.setString(6,f1.getTxtID().getText());
            ps.execute();
            Load();          
        }catch( NumberFormatException | SQLException h) {
            System.out.println("Co loi khi update: "+h.getMessage());
        }
              }
          });
      }
      
      private void xulyDelete(){
          f1.getBtnDelete().addActionListener(new ActionListener() {
              @Override
              public void actionPerformed(ActionEvent e) {
              int ans;
                  ans = JOptionPane.showConfirmDialog(f1,"Do you want to delete"+f1.getTxtID().getName(),"Delete Mes",0);
        if(ans==0){
        String sql = "delete from StudentInfo where ID =? ";
            try{
                PreparedStatement ps = con.prepareStatement(sql);
                ps.setString(1,f1.getTxtID().getText());
                ps.execute();
                Load();  
                f1.getTxtID().setText(f1.getTxtID().getText());
            }catch(SQLException g){
                System.out.println("Co loi khi delete: "+g.getMessage());
            }
        }
      }
      });
    }
      
      public static void main(String[] args) {
        new MainController(new LoadToTable()).control();
    }

}

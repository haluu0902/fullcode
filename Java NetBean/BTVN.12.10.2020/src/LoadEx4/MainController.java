
package LoadEx4;

import context.DBContext;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Vector;
import javax.swing.DefaultComboBoxModel;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author LENOVO
 */
public class MainController {
     LoadToTableEx4 f1;
    
    public MainController(LoadToTableEx4 f1) {
        this.f1 = f1;
    }

    public MainController() {    
    }
    
    private void control(){
        f1.setVisible(true);
        initConnection(); 
        initCbxSearch();
        btnLoad();
        xulySearch();
    }
    
    Connection con;
    DefaultTableModel dftm = new DefaultTableModel();
    HashSet<String> hs;
   
    private void initConnection() {
        try{
            con = new DBContext().getConnection();
            System.out.println("Ket noi thanh cong");
        } catch (Exception e){
            System.out.println("Ket noi that bai" + e.getMessage());
        }
    }
    
    String[] title={"ID", "Full Name", "Gender", "DepartName", "GPA", "Address"};
    String [] SearchField = {"s.ID", "s.Name", "s.Gender", "d.DepartName", "s.GPA", "s.Address"};
    String ss = "select "+SearchField[0];
    {
    for(int i=1;i<SearchField.length;i++){
        ss = ss+", "+SearchField[i];
    }
    ss = ss+ " from StudentInfor s, DepartInfor d where s.DepartID=d.DepartID";
        System.out.println(ss);
    }
    
    private void initCbxSearch(){
        f1.getCbxSearchIn().setModel(new DefaultComboBoxModel<>(title));
        f1.getCbxSearchIn().setSelectedIndex(0);
    }
    private void Load(){
        Load(ss);
    }
    
    private void Load(String sql){
        dftm.setColumnIdentifiers(title);
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
                vec.add(rs.getBoolean(3));            
                vec.add(rs.getString(4));
                vec.add(rs.getFloat(5));
                vec.add(rs.getString(6));
                dftm.addRow(vec);
            }
            f1.getTblDisplay().setModel(dftm);
            int n = dftm.getRowCount();
            if(n==0) f1.getLblDisplay().setText("Khong co ban ghi");
            else f1.getLblDisplay().setText("Da tim thay "+n+" ban ghi");
        } catch(Exception e){
            System.out.println("Co loi" +e.getMessage());
        }
    } 
    
    private void xulySearch() {
        f1.getBtnSearch().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int n= f1.getCbxSearchIn().getSelectedIndex();
                 ArrayList <Integer>ar = new ArrayList();
                if(n==0){}
            else{
                String sql = ss+" and ("+SearchField[n]+" like '%"+f1.getTxtSearchIn().getText()+"%'";
                if(n>1)
                    for(int i=1;i<n;i++)
                        sql = sql+" or "+SearchField[n]+" like '%"+f1.getTxtSearchIn().getText()+"%'";
                    sql=sql+")";
                System.out.println(sql);
                Load(sql);
        }
    }
        });
    }
    
    private void btnLoad(){
        f1.getBtnLoad().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Load();
            }
        });
    }
    
    public static void main(String[] args) {
        new MainController(new LoadToTableEx4()).control();
    }    
}
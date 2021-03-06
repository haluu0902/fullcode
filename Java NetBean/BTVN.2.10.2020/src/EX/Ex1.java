/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package EX;

import context.DBContext;
import java.sql.*;
import java.util.HashSet;
import java.util.Vector;
import javax.swing.DefaultComboBoxModel;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author LENOVO
 */
public class Ex1 extends javax.swing.JFrame {

    /**
     * Creates new form LoadTable
     */
    public Ex1() {
        initComponents();
        initConnection();
        loadDepartName();
    }
    Connection con;
    DefaultTableModel dftm = new DefaultTableModel();
    HashSet<String> hs;
    
    private void TableAction(){
        tblDisplay.getSelectionModel().addListSelectionListener(new ListSelectionListener() {
            @Override
            public void valueChanged(ListSelectionEvent e) {
               int n = tblDisplay.getSelectedRow();
               txtID.setText(tblDisplay.getValueAt(n, 0)+"");
               txtName.setText(tblDisplay.getValueAt(n, 1)+"");
               String selected = tblDisplay.getValueAt(n, 2)+"";
               cbMale.setSelected(selected.equals("true"));
               cbFemale.setSelected(selected.equals("false"));
               lstDepartName.setSelectedValue(tblDisplay.getValueAt(n, 3)+"" ,true);
               txtGPA.setText(tblDisplay.getValueAt(n, 4)+"");
               txtAddress.setText(tblDisplay.getValueAt(n, 5)+"");
            }
        });
    }
    private void loadDepartName(){
        String sql="Select * from DepartInfor";
        Vector vec = new Vector();
        try{
            PreparedStatement ps = con.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                vec.add(rs.getString(2));
            }
            lstDepartName.setModel(new DefaultComboBoxModel<String>(vec));
        }catch (Exception e){
            
        }
    }
    private void initConnection() {
        try {
            con = new DBContext().getConnection();
            System.out.println("Ket noi thanh cong");
        } catch (Exception e) {
            System.err.println("Ket noi that bai" + e.getMessage());
        }
    }
    private void Load() {
    String[]tittle={"ID", "Full Name","Gender","DepartName","GPA","Address"};
          dftm.setColumnIdentifiers(tittle);
          String sql ="Select s.ID,s.Name,s.Gender,d.DepartName,s.GPA,s.[Address] from StudentInfo s , DepartInfor d\n" +
                        "where s.DepartID=d.DepartID";
          try{
              PreparedStatement ps = con.prepareStatement(sql);
              ResultSet rs = ps.executeQuery();
              Vector vec;
              hs = new HashSet<String>();
              while(rs.next()){
                  vec=new Vector();
                  vec.add(rs.getString(1));
                  hs.add(rs.getString(1));
                  vec.add(rs.getString("Name"));
                  vec.add(rs.getBoolean("Gender"));
                  vec.add(rs.getString(4));
                  vec.add(rs.getString(5));
                  vec.add(rs.getString(6));
                  dftm.addRow(vec);
              }
              tblDisplay.setModel(dftm);
          }catch(Exception e){
              System.out.println("Co loi"+e.getMessage());
          }
    }
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jScrollPane1 = new javax.swing.JScrollPane();
        tblDisplay = new javax.swing.JTable();
        BtnLoad = new javax.swing.JButton();
        txtID = new javax.swing.JTextField();
        txtName = new javax.swing.JTextField();
        jScrollPane2 = new javax.swing.JScrollPane();
        txtAddress = new javax.swing.JTextArea();
        txtGPA = new javax.swing.JTextField();
        cbMale = new javax.swing.JCheckBox();
        cbFemale = new javax.swing.JCheckBox();
        jScrollPane3 = new javax.swing.JScrollPane();
        lstDepartName = new javax.swing.JList<>();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        tblDisplay.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            new String [] {
                "Title 1", "Title 2", "Title 3", "Title 4"
            }
        ));
        jScrollPane1.setViewportView(tblDisplay);

        BtnLoad.setText("Load");
        BtnLoad.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BtnLoadActionPerformed(evt);
            }
        });

        txtID.addCaretListener(new javax.swing.event.CaretListener() {
            public void caretUpdate(javax.swing.event.CaretEvent evt) {
                txtIDCaretUpdate(evt);
            }
        });

        txtAddress.setColumns(20);
        txtAddress.setRows(5);
        jScrollPane2.setViewportView(txtAddress);

        txtGPA.setText("0");

        cbMale.setText("Male");

        cbFemale.setText("Female");

        lstDepartName.setModel(new javax.swing.AbstractListModel<String>() {
            String[] strings = { "Item 1", "Item 2", "Item 3", "Item 4", "Item 5" };
            public int getSize() { return strings.length; }
            public String getElementAt(int i) { return strings[i]; }
        });
        jScrollPane3.setViewportView(lstDepartName);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(47, 47, 47)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 580, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(297, 297, 297)
                        .addComponent(BtnLoad))
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(cbFemale)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(txtName, javax.swing.GroupLayout.PREFERRED_SIZE, 171, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(cbMale))
                                .addGap(99, 99, 99)
                                .addComponent(jScrollPane3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addComponent(txtID, javax.swing.GroupLayout.PREFERRED_SIZE, 121, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(84, 84, 84)
                                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 210, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(txtGPA, javax.swing.GroupLayout.PREFERRED_SIZE, 48, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(96, 96, 96)))))
                .addContainerGap(42, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 275, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(txtID, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(33, 33, 33)
                                .addComponent(txtName, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 36, Short.MAX_VALUE)
                                .addComponent(cbMale)
                                .addGap(29, 29, 29)
                                .addComponent(cbFemale))
                            .addGroup(layout.createSequentialGroup()
                                .addGap(18, 18, 18)
                                .addComponent(txtGPA, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addGap(75, 75, 75))
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jScrollPane3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(BtnLoad))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void BtnLoadActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BtnLoadActionPerformed
        Load();
        TableAction();
    }//GEN-LAST:event_BtnLoadActionPerformed

    private void txtIDCaretUpdate(javax.swing.event.CaretEvent evt) {//GEN-FIRST:event_txtIDCaretUpdate

    }//GEN-LAST:event_txtIDCaretUpdate

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Ex1.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Ex1.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Ex1.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Ex1.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Ex1().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton BtnLoad;
    private javax.swing.JCheckBox cbFemale;
    private javax.swing.JCheckBox cbMale;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JScrollPane jScrollPane3;
    private javax.swing.JList<String> lstDepartName;
    private javax.swing.JTable tblDisplay;
    private javax.swing.JTextArea txtAddress;
    private javax.swing.JTextField txtGPA;
    private javax.swing.JTextField txtID;
    private javax.swing.JTextField txtName;
    // End of variables declaration//GEN-END:variables
}

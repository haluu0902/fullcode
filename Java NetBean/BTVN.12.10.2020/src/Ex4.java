
import context.DBContext;
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
 * @author LTTH
 */
public class Ex4 extends javax.swing.JFrame {

    /**
     * Creates new form Ex4
     */
    public Ex4() {
        initComponents();
        initConnection();
        initCbxSearch();
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
    ss = ss+ " from StudentInfo s, DepartInfo d where s.DepartID=d.DepartID";
        System.out.println(ss);
    }
    
    private void initCbxSearch(){
        cbxSearchIn.setModel(new DefaultComboBoxModel<>(title));
        cbxSearchIn.setSelectedIndex(0);
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
            tblDisplay.setModel(dftm);
            int n = dftm.getRowCount();
            if(n==0) lblDisplay.setText("Khong co ban ghi");
            else lblDisplay.setText("Da tim thay "+n+" ban ghi");
        } catch(Exception e){
            System.out.println("Co loi" +e.getMessage());
        }
    } 
    
    private void Search(){
        int n= cbxSearchIn.getSelectedIndex();
        ArrayList <Integer>ar = new ArrayList();
        
 
        if(n==0){}
        else{
            String sql = ss+" and ("+SearchField[n]+" like '%"+txtSearchIn.getText()+"%'";
            if(n>1)
                for(int i=1;i<n;i++)
                    sql = sql+" or "+SearchField[n]+" like '%"+txtSearchIn.getText()+"%'";
                sql=sql+")";
            System.out.println(sql);
            Load(sql);
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
        btnLoad = new javax.swing.JButton();
        txtSearchIn = new javax.swing.JTextField();
        chkSearchAll = new javax.swing.JCheckBox();
        btnSearch = new javax.swing.JButton();
        cbxSearchIn = new javax.swing.JComboBox<>();
        lblDisplay = new javax.swing.JLabel();

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

        btnLoad.setText("Load");
        btnLoad.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnLoadActionPerformed(evt);
            }
        });

        txtSearchIn.setText("n");

        chkSearchAll.setText("Search All");

        btnSearch.setText("Search");
        btnSearch.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnSearchActionPerformed(evt);
            }
        });

        cbxSearchIn.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Item 1", "Item 2", "Item 3", "Item 4" }));

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jScrollPane1)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(txtSearchIn, javax.swing.GroupLayout.PREFERRED_SIZE, 128, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(cbxSearchIn, javax.swing.GroupLayout.PREFERRED_SIZE, 86, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(chkSearchAll, javax.swing.GroupLayout.PREFERRED_SIZE, 128, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(btnLoad)
                        .addGap(18, 18, 18)
                        .addComponent(btnSearch))
                    .addComponent(lblDisplay, javax.swing.GroupLayout.PREFERRED_SIZE, 236, javax.swing.GroupLayout.PREFERRED_SIZE)))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 117, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(txtSearchIn, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(cbxSearchIn, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnLoad)
                    .addComponent(btnSearch))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(chkSearchAll)
                    .addComponent(lblDisplay, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnLoadActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnLoadActionPerformed
        Load();       
    }//GEN-LAST:event_btnLoadActionPerformed

    private void btnSearchActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnSearchActionPerformed
        Search();
    }//GEN-LAST:event_btnSearchActionPerformed

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
            java.util.logging.Logger.getLogger(Ex4.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Ex4.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Ex4.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Ex4.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Ex4().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnLoad;
    private javax.swing.JButton btnSearch;
    private javax.swing.JComboBox<String> cbxSearchIn;
    private javax.swing.JCheckBox chkSearchAll;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JLabel lblDisplay;
    private javax.swing.JTable tblDisplay;
    private javax.swing.JTextField txtSearchIn;
    // End of variables declaration//GEN-END:variables

}
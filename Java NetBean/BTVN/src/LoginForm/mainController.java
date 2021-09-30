/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LoginForm;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 *
 * @author LENOVO
 */
public class mainController {
    firstform f1;
    secondform f2;
    
    public mainController(firstform f1, secondform f2){
        this.f1 = f1;
        this.f2 = f2;
    }
    
    public void control(){
        f1.setVisible(true);
        xulybtnFormat();
        xulybtnOK();
    }
    
    public void xulybtnOK(){
        f2.getBtnOK().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String username = f2.getTxtUsername().getText();
                String password = f2.getTxtPassword().getText();
                boolean select = f2.getChkRemember().isSelected();
                f1.getTxtDisplay().setText(username + "\n" + password + "\n" + (select? "Yes":"No"));
                f2.setVisible(false);
                f1.setVisible(true);
            }
        });
    }
    
    /*String username;
    String password;
    boolean select;*/
    private void xulybtnFormat(){
        f1.getBtnLogin().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                /*username = f2.getTxtUsername().getText();
                f1.getTxtDisplay().setText(username);
                password = f2.getTxtPassword().getText();
                f1.getTxtDisplay().setText(password);
                select = f2.getChkRemember().isSelected();
                f1.getTxtDisplay().setText(select? "Yes":"No");*/
                f1.setVisible(false);
                f2.setVisible(true);
            }
        });
    }
    
    public static void main(String[] args) {
        new mainController(new firstform(), new secondform()).control(); 
    }
}



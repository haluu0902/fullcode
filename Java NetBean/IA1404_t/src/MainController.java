
import java.awt.Dimension;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.Insets;
import javax.swing.JButton;
import javax.swing.text.View;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public class MainController {
    Caro v;
    JButton [][] btn;
    int sizeOfBoard, sizeOfCell = 40;
    boolean whoMove = true, canPlay = true;

    public MainController(Caro v) {
        this.v = v;
    }
    
    public void control(){
        v.setVisible(true);
        xylybtnDraw();
    }
    
    public void xylybtnDraw(){
        v.getBtnDraw().addActionListener((evt)->{
            sizeOfBoard = (int)v.getSpnSize().getValue();
            btn = new JButton[sizeOfBoard][sizeOfBoard];
            v.getPnlDisplay().setSize(sizeOfBoard*sizeOfCell,sizeOfBoard*sizeOfCell);
            v.getPnlDisplay().setLayout(new GridLayout(sizeOfBoard,sizeOfBoard,0,0));
            for (int i = 0; i < sizeOfBoard; i++) {
                for (int j = 0; j < sizeOfBoard; j++) {
                    btn[i][j] = new JButton(" ");
                    btn[i][j].setPreferredSize(new Dimension(sizeOfCell,sizeOfCell));
                    btn[i][j].setMargin(new Insets(2,2,2,2));
                    if(canPlay){
                        final int ii = i, jj = j;
                        btn[i][j].addActionListener((evt1)->{
                            
                        });
                    }
                    v.getPnlDisplay().add(btn[i][j]);
                }
            }
            v.setVisible(true);
        });
        
    }
    
    String draw(boolean x){
        return "<html><span color = '" ;
    }
    
    public static void main(String[] args) {
        new MainController(new Caro()).control();
    }
}

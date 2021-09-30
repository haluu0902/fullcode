/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Realapp;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 *
 * @author PH
 */
public class Control {
    Ex1 f1;
    Ex2 f2;
    public Control(Ex1 f1, Ex2 f2){
        this.f1 = f1;
        this.f2 = f2;
    }
    public void MainControl(){
        f1.setVisible(true);
        actionBtnFormat();
    }
    String text;
    Font font;
    Color color, background;
    private void actionBtnFormat(){
        f1.getBtnFormat().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                text = f1.getLblDisplay().getText();
                f2.getLblDisplay().setText(text);
                font = f1.getLblDisplay().getFont();
                f2.getLblDisplay().setFont(font);
                color = f1.getLblDisplay().getForeground();
                f2.getLblDisplay().setForeground(color);
                background = f1.getLblDisplay().getBackground();
                f2.getLblDisplay().setBackground(background);
                f1.setVisible(true);
                f2.setVisible(true);
            }
        });
    }
    public static void main(String[] args) {
        new Control(new Ex1(), new Ex2()).MainControl();
    }
}

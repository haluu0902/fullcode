/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


class Print{
    int n;

    public Print(int n) {
        this.n = n;
    }
    synchronized void print(String name){
        for (int i = 0; i < n; i++) {
            System.out.println("Thread " + name + " = " + i);
        }
    }
}

class MyThread extends Thread{
    Print p;
    String name;
    MyObject my;

    public MyThread(Print p, String name, MyObject my) {
        this.p = p;
        this.name = name;
        this.my = my;
    }
    public void run(){
        p.print(name);
    }
}

class MyObject{
    
}

class DemoSync{
    public static void main(String[] args) {
        Print p = new Print(100);
        MyObject my = new MyObject();
        MyThread t1 = new MyThread(p, "T1", my);
        MyThread t2 = new MyThread(p, "T2", my);
        MyThread t3 = new MyThread(p, "T3", my);
        t1.start();
        t2.start();
        t3.start();
    }
}
/**
 *
 * @author PH
 */
//public class DemoSync extends Thread{
//    int sum = 0;
//    int begin,end;
//    String name;
//
//    public DemoSync(int begin, int end, String name) {
//        this.begin = begin;
//        this.end = end;
//        this.name = name;
//    }
//    public void run(){
//        for(int i = begin; i <= end; i++){
//            if(check(i))
//                sum+=i;
//        }
//    }
//    private boolean check(int i){
//        return true;
//    }
//}
//
//class Using{
//    public static void main(String[] args) {
//        int n = 1000;
//        DemoSync t1 = new DemoSync(1, n, "T1");
//        DemoSync t2 = new DemoSync(n+1, 2*n, "T2");
//        DemoSync t3 = new DemoSync(2*n+1, 3*n, "T3");
//        t1.start();
//        t2.start();
//        t3.start();
//        
//        while(t1.isAlive() || t2.isAlive() || t3.isAlive()){
//            try {
//                Thread.sleep(0,1);
//            } catch (Exception e) {
//            }
//        }
//        
////        try {
////            t1.join();
////            t2.join();
////            t3.join();
////        } catch (InterruptedException e) {
////        }
//        
//        try {
//            Thread.sleep(500);
//        } catch (Exception e) {
//        }
//        System.out.println("Ket qua thread "+ t1.name +" = " + t1.sum);
//        System.out.println("Ket qua thread "+ t2.name +" = " + t2.sum);
//        System.out.println("Ket qua thread "+ t3.name +" = " + t3.sum);
//    }
//}


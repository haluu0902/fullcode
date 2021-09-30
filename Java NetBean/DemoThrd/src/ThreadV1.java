///*
// * To change this license header, choose License Headers in Project Properties.
// * To change this template file, choose Tools | Templates
// * and open the template in the editor.
// */
//
///**
// *
// * @author PH
// */
//public class ThreadV1 extends Thread{
//    int count = 0;
//
//    @Override
//    public void run() {
//        while(true){
//            System.out.println("Hello " + count++);
//            try {
//                Thread.sleep(500);
//            } catch (Exception e) {
//            }
//        }
//    }
//}
//class UsingThread{
//    public static void main(String[] args) {
////        Thread t = new ThreadV1();
////        t.start();
//        new ThreadV1(){
//            int count = 0;
//            public void run(){
//                while(true){
//                    System.out.println("In Main " + count++);
//                    try {
//                        Thread.sleep(1000);
//                    } catch (Exception e) {
//                    }
//                }
//            }
//        }.start();        
//    }
//}


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author PH
 */
public class ThreadV1 implements Runnable{
    int count = 0;

    @Override
    public void run() {
        while(true){
            System.out.println("Hello " + count++);
            try {
                Thread.sleep(500);
            } catch (Exception e) {
            }
        }
    }
}
class UsingThread{
    public static void main(String[] args) {
        new Thread(()->{
            int count = 0;
            while(true){
                System.out.println("Hello " + count++);
                try {
                    Thread.sleep(500);
                } catch (Exception e) {
                }
            }
        }).start();
    }
}

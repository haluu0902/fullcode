/**
 *
 * @author Admin
 */
public class MainQ1 {
    public static void main(String[] args) {
        int a [] = {6, -8, 15, 3, 2, -5};
        IntList list = new IntList();
        
        System.out.println("Output: Task 1 (1 point)");
        for(int x : a)
            list.addToHead(x);
        list.displayAll();
        
        System.out.println("\nOutput: Task 2 (1 point)");
        list.clear();
        for(int x : a)
            list.addToTail(x);
        list.displayAll();
        System.out.println("Min: " + list.min());
        
        System.out.println("\nOutput: Task 3 (1 point)");
        list.clear();
        for(int x : a)
            list.addToTail(x);
        list.displayAll();
        list.dele2thPos();
        list.displayAll();
        
        System.out.println("\nOutput: Task 4 (1 point)");
        list.clear();
        for(int x : a)
            list.addToTail(x);
        list.displayAll();
        list.search(3);
        list.search(4);
        
        System.out.println("\nOutput: Task 5 (1 point)");
        list.clear();
        for(int x : a)
            list.addToTail(x);
        list.displayAll();
        list.sortPositive();
        list.displayAll(); 
        
        System.out.println("\nOutput: Task 6 (1 point)");
        list.clear();
        for(int x : a)
            list.addToTail(x);
        list.displayAll();
        System.out.println("Quantity of Positive Number: " + list.count()); ;
    }
}

        

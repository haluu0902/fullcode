public class Ex1 {
    public static void main(String[] args) {
        int a[] = new int[] {15, 17, 20, 8, 4, 10, 2, 12, 16};
        BinTree tree = new BinTree();   
        for (int x : a)
            tree.insert(x); 
        tree.breadthTraverse(); System.out.println("");
        tree.inOrder();
        System.out.println("Count = " + tree.count());
        
        // ReBalance tree
        tree.reBalance();
        tree.inOrder();             System.out.println("");
        tree.breadthTraverse();
    }    
}
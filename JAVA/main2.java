public class Fibonacci {
    public static void main(String[] args) {
        int n = 10, first = 0, second = 1;
        System.out.println("Fibonacci Series till " + n + " terms:");
        
        for (int i = 1; i <= n; ++i) {
            System.out.print(first + " ");
            
            // compute next term
            int next = first + second;
            first = second;
            second = next;
        }
    }
}

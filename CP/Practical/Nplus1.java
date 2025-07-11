import java.util.Scanner;
public class Nplus1 {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    while (n != 1) {
      System.out.print(n + " ");
      n = n % 2 == 0 ? n / 2 : 3 * n + 1;
    }
    System.out.print(1);
  }
}

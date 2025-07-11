import java.util.Scanner;
class Multiplication_game {
  public static void main(String[] a) {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNextLong()) {
      long n = sc.nextLong(), turn = 1;
      long p = 1;
      while (p < n) {
        p *= (turn % 2 == 1) ? 9 : 2;
        turn++;
      }
      System.out.println((turn % 2 == 0) ? "Stan wins." : "Ollie wins.");
    }
  }
}
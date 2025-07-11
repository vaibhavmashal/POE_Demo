import java.util.Scanner;
class Ones {
  public static void main(String[] a) {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNextInt()) {
      int n = sc.nextInt(), rem = 1, len = 1;
      while (rem % n != 0) {
        rem = (rem * 10 + 1) % n;
        len++;
      }
      System.out.println(len);
    }
  }
}
import java.util.Scanner;
class Reverse_Add {
  static int reverse(int n) {
    int r = 0;
    while (n > 0) {
      r = r * 10 + n % 10;
      n /= 10;
    }
    return r;
  }
  public static void main(String[] a) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    while (t-- > 0) {
      int n = sc.nextInt(), cnt = 0;
      while (true) {
        int rev = reverse(n);
        if (n == rev) break;
        n += rev; cnt++;
      }
      System.out.println(cnt + " " + n);
    }
  }
}

// using StringBuilder

// import java.util.*;
// public class Main {
//   static boolean isPal(String s) {
//     return s.equals(new StringBuilder(s).reverse().toString());
//   }
//   public static void main(String[] args) {
//     Scanner s = new Scanner(System.in);
//     int t = s.nextInt();
//     while (t-- > 0) {
//       int c = 0;
//       String n = s.next();
//       while (!isPal(n)) {
//         String r = new StringBuilder(n).reverse().toString();
//         n = Long.toString(Long.parseLong(n) + Long.parseLong(r));
//         c++;
//       }
//       System.out.println(c + " " + n);
//     }
//   }
// }

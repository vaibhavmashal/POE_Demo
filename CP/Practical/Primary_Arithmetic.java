import java.util.*;
class Primary_Arithmetic {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    while (true) {
      int a = sc.nextInt(), b = sc.nextInt();
      if (a == 0 && b == 0) break;
      int carry = 0, c = 0;
      while (a > 0 || b > 0) {
        carry += a % 10 + b % 10;
        if (carry >= 10) { c++; carry = 1; }
        else carry = 0;
        a /= 10; b /= 10;
      }
      System.out.println(c == 0 ? "No carry operation." :
        c + " carry operation" + (c > 1 ? "s." : "."));
    }
  }
}
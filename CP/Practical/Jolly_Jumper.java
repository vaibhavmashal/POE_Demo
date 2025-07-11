import java.util.*;
public class Jolly_Jumper {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int n = s.nextInt(), a[] = new int[n];
    for (int i = 0; i < n; i++) a[i] = s.nextInt();
    boolean[] d = new boolean[n];
    for (int i = 1; i < n; i++) {
      int diff = Math.abs(a[i] - a[i - 1]);
      if (diff < n) d[diff] = true;
    }
    for (int i = 1; i < n; i++) if (!d[i]) {
      System.out.print("Not jolly");
      return;
    }
    System.out.print("Jolly");
  }
}

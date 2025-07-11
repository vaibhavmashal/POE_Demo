import java.util.*;
public class Hartals {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    while (T-- > 0) {
      int n = sc.nextInt(), p = sc.nextInt(), count = 0;
      boolean[] days = new boolean[n + 1];
      for (int i = 0; i < p; i++) {
        int h = sc.nextInt();
        for (int d = h; d <= n; d += h)
          if (!days[d] && d % 7 != 6 && d % 7 != 0) {
            days[d] = true;
            count++;
          }
      }
      System.out.println(count);
    }
  }
}

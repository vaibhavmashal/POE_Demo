import java.util.*;
import java.math.BigInteger;
public class Polynomial_co {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNextInt()) {
      int n = sc.nextInt(), k = sc.nextInt();
      BigInteger res = BigInteger.ONE;
      for (int i = 2; i <= n; i++) res = res.multiply(BigInteger.valueOf(i));
      for (int i = 0; i < k; i++) {
        int x = sc.nextInt();
        for (int j = 2; j <= x; j++) res = res.divide(BigInteger.valueOf(j));
      }
      System.out.println(res);
    }
  }
}

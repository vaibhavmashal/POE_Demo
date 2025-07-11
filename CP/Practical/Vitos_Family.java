import java.util.*;
class Vitos_Family {
  public static void main(String[] a) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    while (t-- > 0) {
      int n = sc.nextInt(), arr[] = new int[n];
      for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
      Arrays.sort(arr);
      int m = arr[n / 2], sum = 0;
      for (int x : arr) sum += Math.abs(x - m);
      System.out.println(sum);
    }
  }
}
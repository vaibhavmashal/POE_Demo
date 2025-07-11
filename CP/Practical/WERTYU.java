import java.util.*;
class WERTYU {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String map = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./";
    while (sc.hasNextLine()) {
      String l = sc.nextLine(), r = "";
      for (char c : l.toCharArray()) {
        int i = map.indexOf(c);
        r += (i > 0) ? map.charAt(i - 1) : c;
      }
      System.out.println(r);
    }
  }
}
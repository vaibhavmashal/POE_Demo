import java.util.*;
class Common_Perm {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNextLine()) {
      String a = sc.nextLine(), b = sc.nextLine();
      int[] f1 = new int[26], f2 = new int[26];
      for (char c : a.toCharArray()) f1[c - 'a']++;
      for (char c : b.toCharArray()) f2[c - 'a']++;
      StringBuilder sb = new StringBuilder();
      for (int i = 0; i < 26; i++)
        sb.append(String.valueOf((char)(i + 'a')).repeat(Math.min(f1[i], f2[i])));
      System.out.println(sb);
    }
  }
}
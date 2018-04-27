import java.io.*;
import java.util.*;

public class ac {
  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), ans = -Integer.MAX_VALUE;
    for (int i = 0; i < n; i++) {
      int x = sc.nextInt();
      ans = Math.max(ans, x);
    }
    System.out.println(ans);
  }
}

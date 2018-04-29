import com.sun.xml.internal.org.jvnet.fastinfoset.FastInfosetException;

import java.io.*;
import java.util.*;

public class Hilldescent {
    static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }
        String next() {
            while (st == null || !st.hasMoreElements())
            { try
                {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException  e)
                {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String nextLine(){
            String str = "";
            try
            {
                str = br.readLine();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return str;
        }
    }
    public static final int MAXM = 1005;
    public static final int MAXN = 1005;

    public static int[][] grid = new int[MAXN][MAXM];
    public static int[][] dp = new int[MAXN][MAXM];
    public static char[][] neighbor = new char[MAXN][MAXM];

    public static int[] max_start = new int[2];

    public static int maximum = -1;
    public static int n,m;

    public static int solve(int row, int col ){
        if (grid[row][col] == -1) // If we are outside, there is no path
            return 0;

        if (dp[row][col] != 0) // If we have already computed, use that
            return dp[row][col];

        dp[row][col] = 1; // If it's not outside the grid, then at the very least there is a distance of 1 there.

        int[] dirs = {row + 1, col, row - 1, col, row, col - 1, row, col + 1}; // all possible directions
        char[] dirs_c = {'S', 'N', 'W', 'E'};                                  // The corresponding letters

        for (int i = 0; i < 8; i += 2)
        {
            if (grid[dirs[i]][dirs[i + 1]] < grid[row][col]) // if the value is downhill we recurese.
            {

                int s = solve(dirs[i], dirs[i + 1]) + 1; // the recursion
                if (s > dp[row][col])                    // we update the length and neighbor from which we came if s is greater
                {
                    dp[row][col] = s;
                    neighbor[row][col] = dirs_c[i / 2];
                }
                else if (s == dp[row][col]) // if s is the same, we make sure we take the neighbor with the lower lexographical value
                {
                    if (dirs_c[i / 2] < neighbor[row][col])
                        neighbor[row][col] = dirs_c[i / 2];
                }
            }
        }

        if (dp[row][col] > maximum) // maximum tracks the longest length.
        {
            maximum = dp[row][col];
            //max_start = make_pair(row, col);r
            max_start[0] = row;
            max_start[1] = col;
        }

        return dp[row][col];
    }
    public static void resetGrid(){
        for (int i = 0; i < MAXN; i ++){
            for (int j = 0; j< MAXM; j++){
                grid[i][j] = -1;
            }
        }
    }
    public static void printPath(){
        int[] p = new int[2];
        p[0] = max_start[0];
        p[1] = max_start[1];
        char dir = neighbor[p[0]][p[1]];
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < maximum; i++){
            sb.append(dir);
            if (dir == 'E'){
                p[1]++;
            } else if (dir == 'W'){
                p[1]--;
            } else if (dir == 'S') {
                p[0]++;
            } else if (dir == 'N'){
                p[0]--;
            }
            dir = neighbor[p[0]][p[1]];
            if (dir == 0) break;
        }
        System.out.println(sb.toString());

    }
    public static void findStart(){
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                if (dp[i][j] == maximum)
                {
                    int row = max_start[0];
                    int col = max_start[1];
                    if (grid[i][j] > grid[row][col]) {
                        max_start[0] = i;
                        max_start[1] = j;
                    }
                }
            }
        }

    }
    public static void main(String args[]){
        resetGrid();
        FastReader fr = new FastReader();
        n = fr.nextInt();
        m = fr.nextInt();
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= m; j++){
                grid[i][j] = fr.nextInt();
            }
        }
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= m; j++){
                System.out.println(grid[i][j]);
            }
        }
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= m; j++){
               solve(i,j);
            }
        }
        if (maximum > 1){
            findStart();
            System.out.println(maximum);
            System.out.println(max_start[0] + " " + max_start[1]);
            printPath();
        } else {
            System.out.println("no descent");
        }

    }
}

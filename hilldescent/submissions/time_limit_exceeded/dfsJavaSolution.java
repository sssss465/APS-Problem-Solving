import java.util.*;

public class dfsJavaSolution {
    public static class HillDescent {
        private static int maxPathX = Integer.MAX_VALUE, maxPathY = Integer.MAX_VALUE;
        private static int maxAltitude = Integer.MIN_VALUE;
        private static int maxPathCount = 0;
        private static String maxPath = "";
        HillDescent(int[][] grid, int n, int m) {
            WeightedDirectedGraph G = buildGraph(grid, n, m);
            for (int v = 0; v < G.vertices; v++) {
                DFS dfs = new DFS(G, v);
                if (dfs.max() >= maxPathCount) {
                    int x = v - (v / m) * m + 1;
                    int y = v / m + 1;
                    int altitude = grid[y - 1][x - 1];
                    // Found same length longest path
                    if (dfs.max() == maxPathCount) {
                        // Found same length longest path but with greater altitude
                        if (altitude > maxAltitude)
                            setNewPath( x, y, dfs.path(), dfs.max(), altitude );
                        // Found same length longest path but with same altitude
                        else if (altitude == maxAltitude) {
                            // Change longest path only if has smaller Y, if Y
                            // is the same, then if has smaller X
                            if (y == maxPathY)
                                if (x < maxPathX)
                                    setNewPath( x, y, dfs.path(), dfs.max(), altitude );
                            else if (y < maxPathY)
                                setNewPath( x, y, dfs.path(), dfs.max(), altitude );
                        }
                    }
                    // Found a longer path
                    else if (dfs.max() > maxPathCount)
                        setNewPath( x, y, dfs.path(), dfs.max(), altitude );
                }
            }
        }
        private static WeightedDirectedGraph buildGraph(int[][] grid, int n, int m) {
            WeightedDirectedGraph g = new WeightedDirectedGraph(n, m);
            for (int row = 0; row < n; row++) {
                for (int col = 0; col < m; col++) {
                    int index = row * m + col;
                    if (col < m - 1) g.addEdge(index, index + 1, grid[row][col + 1] - grid[row][col]);
                    if (row > 0) g.addEdge(index, index - m, grid[row - 1][col] - grid[row][col]);
                    if (col > 0) g.addEdge(index, index - 1, grid[row][col - 1] - grid[row][col]);
                    if (row < n - 1) g.addEdge(index, index + m, grid[row + 1][col] - grid[row][col]);
                }
            }
            return g;
        }
        private static void setNewPath(int x, int y, String newPath, int count, int altitude) {
            maxPathX = x;
            maxPathY = y;
            maxPath = newPath;
            maxPathCount = count;
            maxAltitude = altitude;
        }
        public String getPath() { return maxPath; }
        public int getPathX() { return maxPathX; }
        public int getPathY() { return maxPathY; }
    }
    public static class Edge {
        int source, destination, weight;
        Edge(int from, int to, int w) {
            source = from;
            destination = to;
            weight = w;
        }
    }
    public static class Node {
        ArrayList<Edge> adjacent = new ArrayList<Edge>();
    }
    public static class WeightedDirectedGraph {
        Node[] list;
        int vertices;
        int rows;
        int cols;
        WeightedDirectedGraph(int n, int m) {
            rows = n;
            cols = m;
            vertices = n * m;
            list = new Node[vertices];
            for (int i = 0; i < vertices; i++) list[i] = new Node();
        }
        public void addEdge(int from, int to, int weight) {
            Edge e = new Edge(from, to, weight);
            list[from].adjacent.add(e);
        }
        public ArrayList<Edge> adj(int v) { return list[v].adjacent; }
    }
    public static class DFS {
        private int maxLength = 0;
        private String maxPath = "";
        DFS(WeightedDirectedGraph G, int s) {
            dfs(G, s, 0, "");
        }
        private void dfs(WeightedDirectedGraph G, int v, int level, String path) {
            boolean lowest = true;
            StringBuilder temp = new StringBuilder(path);
            for (Edge w : G.adj(v)) {
                if (w.weight < 0) {
                    lowest = false;
                    if (v - 1 == w.destination) path = temp + "W";
                    if (v - G.cols == w.destination) path = temp + "N";
                    if (v + 1 == w.destination) path = temp + "E";
                    if (v + G.cols == w.destination) path = temp + "S";
                    dfs(G, w.destination, level + 1, path);
                }
            }
            if (lowest) {
                if (level > maxLength) {
                    maxLength = level;
                    maxPath = path;
                }
                if (maxPath.isEmpty()) {
                    maxPath = path;
                }
                else if (level == maxLength) {
                    if (path.compareTo(maxPath) < 0) maxPath = path;
                }
            }
        }
        public int max() { return maxLength; }
        public String path() { return maxPath; }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {
                grid[row][col] = sc.nextInt();
            }
        }
        HillDescent hd = new HillDescent( grid, n, m );
        if (hd.getPath().isEmpty()) System.out.println("no descent");
        else System.out.println( hd.getPathY() + " " + hd.getPathX() + "\n" + hd.getPath() );
    }
}

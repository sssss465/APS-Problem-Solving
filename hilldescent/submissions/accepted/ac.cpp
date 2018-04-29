#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <functional>
#include <set>
#include <bitset>
#include <unordered_set>
#include <string.h>
#include <ctime>

using namespace std;
typedef long long int ll;
#define REP(i, n) for (int i = 0; i < n; i++)
#define MAXM 1005
#define MAXN 1005
#define MAX_LL 9223372036854775807ll
#define MAX_INT 2147483647

int grid[MAXN][MAXM]; // Where the grid is stored
int n, m;             // size of grid

int dp[MAXN][MAXM];        // Here we store the length of the longest path to that gridpoint
char neighbor[MAXN][MAXM]; // Here we store the next letter in the sequence.
pair<int, int> max_start;  // The coordinate of the starting position.
int maximum = -1;          // Where we store the longest downhill path

int solve(int row, int col)
{
    if (grid[row][col] == -1) // If we are outside, there is no path
        return 0;

    if (dp[row][col] != 0) // If we have already computed, use that
        return dp[row][col];

    dp[row][col] = 1; // If it's not outside the grid, then at the very least there is a distance of 1 there.

    int dirs[8] = {row + 1, col, row - 1, col, row, col - 1, row, col + 1}; // all possible directions
    char dirs_c[4] = {'S', 'N', 'W', 'E'};                                  // The corresponding letters

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
        max_start = make_pair(row, col);
    }

    return dp[row][col];
}

void resetdp()
{
    REP(i, MAXN)
    REP(j, MAXM)
    dp[i][j] = 0;
}

void resetNeighbor()
{
    REP(i, MAXN)
    REP(j, MAXM)
    neighbor[i][j] = 0;
}

void resetGrid()
{
    REP(i, MAXN)
    REP(j, MAXM)
    grid[i][j] = -1;
}

void printPath()
{
    pair<int, int> p = max_start;
    char dir = neighbor[p.first][p.second];
    string str = "";
    for (int i = 0; i < maximum; i++)
    {
        str += dir;
        if (dir == 'E')
            p = make_pair(p.first, p.second + 1);
        else if (dir == 'W')
            p = make_pair(p.first, p.second - 1);
        else if (dir == 'S')
            p = make_pair(p.first + 1, p.second);
        else if (dir == 'N')
            p = make_pair(p.first - 1, p.second);
        dir = neighbor[p.first][p.second];
    }
    printf("%s\n", str.c_str());
}

void findStart() // Finds the tallest starting point with the longest path.
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (dp[i][j] == maximum)
            {
                int row = max_start.first;
                int col = max_start.second;
                if (grid[i][j] > grid[row][col])
                    max_start = make_pair(i, j);
            }
        }
    }
}

int main()
{
    // clock_t start = clock();
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    resetdp();
    resetGrid();
    resetNeighbor();
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            scanf("%d", &grid[i][j]);
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            solve(i, j);
    if (maximum > 1)
    {
        findStart();
        cout << max_start.first << " " << max_start.second << endl;
        printPath();
    }
    else
    {
        cout << "no descent" << endl;
    }
    // cout << clock() - start << endl;
}

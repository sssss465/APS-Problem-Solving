#include <iostream>

using namespace std;

// This is an incorrect solution that has ans initialized to zero.
// This will get WA if the max is negative.
int main() {
  int n, ans = 0;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    ans = max(ans, a);
  }
  cout << ans << endl;
  return 0;
}

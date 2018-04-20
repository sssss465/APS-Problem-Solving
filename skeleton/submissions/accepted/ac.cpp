#include <iostream>

using namespace std;

int main() {
  int n, ans = -(int)1e9;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    ans = max(ans, a);
  }
  cout << ans << endl;
  return 0;
}

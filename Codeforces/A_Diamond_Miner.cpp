#include <bits/stdc++.h>
using namespace std;

const int mod = 1e9 + 7;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define fastio                    \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0);
#define int long long
#define forab(i, a, b) for (int i = a; i <= b; ++i)
#define forabstep(i, a, b, step) for (int i = a; i <= b; i += step)
#define foreach(c, it) for (auto it = (c).begin(); it != (c).end(); ++it)

// END OF TEMPLATE //

void solve() {
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        int n;
        cin >> n;

        vector<int> miners, mines;

        for (int i = 0; i < 2 * n; ++i) {
            int x, y;
            cin >> x >> y;

            if (x == 0) {
                miners.push_back(abs(y));
            }
            if (y == 0) {
                mines.push_back(abs(x));
            }
        }

        sort(miners.begin(), miners.end());
        sort(mines.begin(), mines.end());

        double result = 0.0;
        for (size_t i = 0; i < miners.size(); ++i) {
            result += sqrt(miners[i] * miners[i] + mines[i] * mines[i]);
        }

        // Set precision to desired decimal places
        std::cout << fixed << setprecision(10) << result << endl;
    }
}

signed main() {
    fastio;
    solve();
}
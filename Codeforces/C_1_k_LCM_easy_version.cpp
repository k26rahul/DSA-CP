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

template <typename T>
void print(const T& arg) {
    cout << arg << endl;
}

template <typename T, typename... Args>
void print(const T& first, const Args&... args) {
    cout << first << ' ';
    print(args...);
}

// END OF TEMPLATE //

void solve() {
    int T;
    cin >> T;

    while (T--) {
        int n, k;
        cin >> n >> k;

        int half_n = n / 2;
        int half_half_n = half_n / 2;

        if (n % 2 == 1) {
            print(1, half_n, half_n);
        } else if (half_n % 2 == 0) {
            print(half_n, half_half_n, half_half_n);
        } else {
            print(2, half_n - 1, half_n - 1);
        }
    }
}

signed main() {
    fastio;
    solve();
}
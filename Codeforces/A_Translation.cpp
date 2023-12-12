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
    string s1, s2;
    cin >> s1 >> s2;

    reverse(s1.begin(), s1.end());

    print(s1 == s2 ? "YES" : "NO");
}

signed main() {
    fastio;
    solve();
}
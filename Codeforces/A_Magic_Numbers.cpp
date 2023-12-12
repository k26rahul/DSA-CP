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
    string num;
    cin >> num;
    int n = num.length();

    bool is_magic_num = true;

    int i = 0;
    while (i < n) {
        if (i + 2 < n && num.substr(i, 3) == "144") {
            i += 3;
            continue;
        }
        if (i + 1 < n && num.substr(i, 2) == "14") {
            i += 2;
            continue;
        }
        if (num[i] == '1') {
            i += 1;
            continue;
        }

        is_magic_num = false;
        break;
    }

    print(is_magic_num ? "YES" : "NO");
}

signed main() {
    fastio;
    solve();
}
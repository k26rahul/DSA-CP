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
    int n;
    cin >> n;

    string team_a = "";
    string team_b = "";

    int goals_a = 0;
    int goals_b = 0;

    string team;
    while (n--) {
        cin >> team;

        if (team_a == "") {
            team_a = team;
        }

        if (team == team_a) {
            goals_a += 1;
        } else {
            team_b = team;
            goals_b += 1;
        }
    }

    print(goals_a > goals_b ? team_a : team_b);
}

signed main() {
    fastio;
    solve();
}
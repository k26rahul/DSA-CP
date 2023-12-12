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
    int n, m;
    cin >> n >> m;

    int task;
    int time = 0;
    int current_house = 1;
    while (m--) {
        cin >> task;

        if (task < current_house) {
            time += n - current_house;
            current_house = 0;
        }

        time += task - current_house;
        current_house = task;
    }

    print(time);
}

signed main() {
    fastio;
    solve();
}
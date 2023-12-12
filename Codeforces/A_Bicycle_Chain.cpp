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

template <typename T>
string vectorToString(const vector<T>& vec) {
    stringstream ss;
    ss << "[ ";

    for (const auto& element : vec) {
        ss << element << " ";
    }

    ss << "]";
    return ss.str();
}

// END OF TEMPLATE //

void solve() {
    int n, m;

    cin >> n;
    vi pedal(n);
    forab(i, 0, n) cin >> pedal[i];
    // print(vectorToString(pedal));

    cin >> m;
    vi rear(m);
    forab(i, 0, m) cin >> rear[i];
    // print(vectorToString(rear));

    int max = 0, max_count = 0;

    print(vectorToString(pedal));
    print(vectorToString(rear));

    for (double p : pedal) {
        for (double r : rear) {
            double r_by_p = r / p;
            int int_r_by_p = r_by_p;

            // print(r, p, r_by_p, int_r_by_p);

            if (r_by_p == int_r_by_p) {
                if (r_by_p > max) {
                    max = r_by_p;
                    max_count = 0;
                }
                if (r_by_p == max) {
                    max_count += 1;
                }
            }
        }
    }

    print(max_count);
}

signed main() {
    fastio;
    solve();
}
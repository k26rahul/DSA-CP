#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        int n;
        cin >> n;

        vector<pair<int, int>> k;
        for (int i = 0; i < n; ++i) {
            int left, right;
            cin >> left >> right;
            k.push_back({left, right});
        }

        sort(k.begin(), k.end(),
             [](const pair<int, int>& a, const pair<int, int>& b) {
                 return a.second > b.second;
             });

        int greetings = 0;
        for (int i = 0; i < n; ++i) {
            int left = k[i].first;
            int right = k[i].second;

            for (int j = i + 1; j < n; ++j) {
                int left2 = k[j].first;
                int right2 = k[j].second;

                if (left < right2) {
                    if (right2 - left >= right2 - left2) {
                        greetings += 1;
                    }
                } else {
                    break;
                }
            }
        }

        cout << greetings << endl;
    }

    return 0;
}

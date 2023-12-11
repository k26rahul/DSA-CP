#include <bits/stdc++.h>
#define int long long
using namespace std;
const int mod = 1e9 + 7;

// Function to solve the problem
void solve() {
    // Input the string
    string input;
    cin >> input;

    // Vectors to store the indexes of uppercase and lowercase letters
    vector<int> uppercase;  // store index of uppercase letters
    vector<int> lowercase;  // store index of lowercase letters

    // Iterate through each character in the input string
    for (int i = 0; i < input.size(); i++) {
        // If the current character is 'B'
        if (input[i] == 'B') {
            // Remove the current letter and the previous uppercase letter
            if (uppercase.size() > 0)
                uppercase.pop_back();  // pop_back() operation erases the last
                                       // element in a vector
        }
        // If the current character is 'b'
        else if (input[i] == 'b') {
            // Remove the current and the previous lowercase letter
            if (lowercase.size() > 0) lowercase.pop_back();
        }
        // If the current character is a lowercase letter
        else if (input[i] >= 'a' and input[i] <= 'z') {
            // Store the index of the current letter in the lowercase vector
            lowercase.push_back(i);
        }
        // If the current character is an uppercase letter
        else if (input[i] >= 'A' and input[i] <= 'Z') {
            // Store the index of the current letter in the uppercase vector
            uppercase.push_back(i);
        }
    }

    // Combine vectors to store indexes of both lowercase and uppercase vectors
    vector<int> combine;
    for (auto x : uppercase) combine.push_back(x);
    for (auto x : lowercase) combine.push_back(x);

    // Sort the combined vector to get the correct order of letters
    sort(combine.begin(), combine.end());

    // Build the answer string using the sorted indexes
    string ans;
    for (auto x : combine) {
        ans += input[x];
    }

    // Output the final answer
    cout << ans << endl;
}

// Main function
signed main() {
    // Input the number of test cases
    int T = 1;
    cin >> T;

    // Loop through each test case and call the solve function
    while (T--) solve();
}

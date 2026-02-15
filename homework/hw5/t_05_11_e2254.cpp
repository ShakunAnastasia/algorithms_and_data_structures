#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

long long R, L, B;
vector<long long> X;
vector<long long> P;

long long calculate_cost(int i, int j) {

    int m = (i + j) / 2;
    long long hub_pos = X[m];

    long long count_left = m - i;
    long long count_right = j - m;

    long long sum_left = P[m] - P[i];
    
    long long sum_right = P[j + 1] - P[m + 1];

    long long cost = (hub_pos * count_left - sum_left) + (sum_right - hub_pos * count_right);

    return cost;
}

bool check(int k) {
    for (int i = 0; i <= R - k; ++i) {
        int j = i + k - 1;
        if (calculate_cost(i, j) <= B) {
            return true;
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> R >> L >> B)) return 0;

    X.resize(R);
    P.resize(R + 1, 0);

    for (int i = 0; i < R; ++i) {
        cin >> X[i];
        P[i + 1] = P[i] + X[i];
    }

    int low = 1, high = R;
    int ans = 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << endl;

    return 0;
}

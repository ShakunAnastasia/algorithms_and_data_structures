#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    long long total_ans = 0;
    long long current_le_count = 0;
    long long current_lt_count = 0;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        if (x <= k) {
            current_le_count++;
        } else {
            total_ans += (current_le_count * (current_le_count + 1)) / 2;
            current_le_count = 0;
        }

        if (x < k) {
            current_lt_count++;
        } else {
            total_ans -= (current_lt_count * (current_lt_count + 1)) / 2;
            current_lt_count = 0;
        }
    }

    total_ans += (current_le_count * (current_le_count + 1)) / 2;
    total_ans -= (current_lt_count * (current_lt_count + 1)) / 2;

    cout << total_ans << endl;

    return 0;
}

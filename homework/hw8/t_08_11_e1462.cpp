#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int count;
    if (!(cin >> count)) return 0;

    vector<int> digits[10];

    for (int i = 0; i < count; ++i) {
        int x;
        cin >> x;
        digits[x % 10].push_back(x);
    }

    bool isFirst = true;
    for (auto& bucket : digits) {
        sort(bucket.begin(), bucket.end());
        for (const int& num : bucket) {
            if (!isFirst) cout << " ";
            cout << num;
            isFirst = false;
        }
    }
    
    cout << "\n";
    return 0;
}

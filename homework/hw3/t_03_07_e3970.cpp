#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> colors(n);
    for (int i = 0; i < n; ++i) {
        cin >> colors[i];
    }

    int m;
    cin >> m;

    while (m--) {
        int target_color;
        cin >> target_color;
        auto range = equal_range(colors.begin(), colors.end(), target_color);
        cout << distance(range.first, range.second) << "\n";
    }

    return 0;
}

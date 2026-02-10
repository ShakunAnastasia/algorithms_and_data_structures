#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    while (cin >> n) {
        vector<int> heights(n);
        for (int i = 0; i < n; ++i) {
            cin >> heights[i];
        }

        int a, b;
        cin >> a >> b;

        int count = 0;
        for (int i = 0; i < n; ++i) {
            if (heights[i] >= a && heights[i] <= b) {
                count++;
            }
        }
        cout << count << "\n";
    }

    return 0;
}

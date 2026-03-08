#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> data(n);
    for (int i = 0; i < n; ++i) {
        cin >> data[i];
    }

    int targetValue = data[0];
    int swapCount = 0;

    for (int i = 0; i < n - 1; ++i) {
        int minIdx = i;
        for (int j = i + 1; j < n; ++j) {
            if (data[j] < data[minIdx]) {
                minIdx = j;
            }
        }

        if (minIdx != i) {
            if (data[i] == targetValue || data[minIdx] == targetValue) {
                swapCount++;
            }
            swap(data[i], data[minIdx]);
        }
    }

    cout << swapCount << endl;

    return 0;
}

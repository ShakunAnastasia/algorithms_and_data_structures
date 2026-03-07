#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;
        bool moved = false;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
            moved = true;
        }
        a[j + 1] = key;

        if (moved) {
            for (int k = 0; k < n; k++) {
                cout << a[k] << (k == n - 1 ? "" : " ");
            }
            cout << endl;
        }
    }

    return 0;
}

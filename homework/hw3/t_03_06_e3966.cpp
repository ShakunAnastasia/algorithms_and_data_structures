#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> collection(n);
    for (int i = 0; i < n; ++i) {
        cin >> collection[i];
    }

    int m;
    if (!(cin >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int k;
        cin >> k;
        
        if (binary_search(collection.begin(), collection.end(), k)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}

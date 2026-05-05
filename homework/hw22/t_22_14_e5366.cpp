#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 50005;
vector<int> adj[MAXN];
int sz[MAXN];
int max_subtree[MAXN];
int n;

void dfs(int u, int p) {
    sz[u] = 1;
    max_subtree[u] = 0;
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            sz[u] += sz[v];
            max_subtree[u] = max(max_subtree[u], sz[v]);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    int min_max_comp = n + 1;
    vector<int> candidates;

    for (int i = 1; i <= n; ++i) {
        int current_max = max(max_subtree[i], n - sz[i]);
        if (current_max < min_max_comp) {
            min_max_comp = current_max;
            candidates.clear();
            candidates.push_back(i);
        } else if (current_max == min_max_comp) {
            candidates.push_back(i);
        }
    }

    sort(candidates.begin(), candidates.end());

    for (int i = 0; i < candidates.size(); ++i) {
        cout << candidates[i] << (i == candidates.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}

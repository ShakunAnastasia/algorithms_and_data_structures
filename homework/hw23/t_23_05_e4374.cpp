#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

struct Edge {
    int to;
    int id;
};

const int MAXN = 10005;
const int MAXM = 100005;

vector<Edge> adj[MAXN];
pair<int, int> edges[MAXM];
ull edge_weight[MAXM];
ull node_xor[MAXN];
bool visited[MAXN];
bool is_tree_edge[MAXM];
int depth[MAXN];

void dfs_tree(int u, int d) {
    visited[u] = true;
    depth[u] = d;
    for (auto& e : adj[u]) {
        if (!visited[e.to]) {
            is_tree_edge[e.id] = true;
            dfs_tree(e.to, d + 1);
        }
    }
}

void dfs_weights(int u, int p_id) {
    visited[u] = true;
    for (auto& e : adj[u]) {
        if (is_tree_edge[e.id] && e.id != p_id) {
            dfs_weights(e.to, e.id);
            node_xor[u] ^= node_xor[e.to];
        }
    }
    if (p_id != -1) {
        edge_weight[p_id] = node_xor[u];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= m; ++i) {
        cin >> edges[i].first >> edges[i].second;
        adj[edges[i].first].push_back({edges[i].second, i});
        adj[edges[i].second].push_back({edges[i].first, i});
    }

    dfs_tree(1, 0);

    mt19937_64 rng(1337);
    for (int i = 1; i <= m; ++i) {
        if (!is_tree_edge[i]) {
            ull w = rng();
            edge_weight[i] = w;
            node_xor[edges[i].first] ^= w;
            node_xor[edges[i].second] ^= w;
        }
    }

    for (int i = 1; i <= n; ++i) visited[i] = false;
    dfs_weights(1, -1);

    int k;
    cin >> k;
    while (k--) {
        int c;
        cin >> c;
        vector<ull> current_weights(c);
        for (int i = 0; i < c; ++i) {
            int edge_idx;
            cin >> edge_idx;
            current_weights[i] = edge_weight[edge_idx];
        }

        bool disconnected = false;
        int subsets = (1 << c);
        for (int i = 1; i < subsets; ++i) {
            ull xor_sum = 0;
            for (int j = 0; j < c; ++j) {
                if ((i >> j) & 1) {
                    xor_sum ^= current_weights[j];
                }
            }
            if (xor_sum == 0) {
                disconnected = true;
                break;
            }
        }

        if (disconnected) cout << "Disconnected\n";
        else cout << "Connected\n";
    }

    return 0;
}

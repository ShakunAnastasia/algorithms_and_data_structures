#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, w, id;
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        edges[i].u--;
        edges[i].v--;
        edges[i].id = i;
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    DSU dsu1(n);
    int s1 = 0;
    int edges_count1 = 0;
    vector<int> mst_edge_ids;

    for (int i = 0; i < m; ++i) {
        if (dsu1.unite(edges[i].u, edges[i].v)) {
            s1 += edges[i].w;
            mst_edge_ids.push_back(edges[i].id);
            edges_count1++;
            if (edges_count1 == n - 1) break;
        }
    }

    int s2 = 2e9;

    for (int banned_id : mst_edge_ids) {
        DSU dsu2(n);
        int current_s = 0;
        int edges_count2 = 0;

        for (int i = 0; i < m; ++i) {
            if (edges[i].id == banned_id) continue;

            if (dsu2.unite(edges[i].u, edges[i].v)) {
                current_s += edges[i].w;
                edges_count2++;
                if (edges_count2 == n - 1) break;
            }
        }

        if (edges_count2 == n - 1) {
            s2 = min(s2, current_s);
        }
    }

    cout << s1 << " " << s2 << "\n";

    return 0;
}

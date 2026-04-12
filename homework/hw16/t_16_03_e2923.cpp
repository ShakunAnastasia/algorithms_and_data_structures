#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#pragma GCC optimize("Ofast")

struct Node {
    int id;
    int color;
    int tin, tout;
    vector<Node*> children;
};

Node nodes[1000005];
int timer = 0;
int dfs_order[1000005];
int bit[1000005];
int last_pos[1000005];
int result[1000005];

void update(int i, int val, int n) {
    for (; i <= n; i += i & -i) bit[i] += val;
}

int query(int i) {
    int s = 0;
    for (; i > 0; i -= i & -i) s += bit[i];
    return s;
}

void buildDFS(Node* v) {
    v->tin = ++timer;
    dfs_order[timer] = v->id;
    for (Node* child : v->children) {
        buildDFS(child);
    }
    v->tout = timer;
}

struct Query {
    int l, r, id;
};

bool compareQueries(const Query& a, const Query& b) {
    if (a.r != b.r) return a.r < b.r;
    return a.l < b.l;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    int root_id = 0;
    for (int i = 1; i <= n; ++i) {
        int p, c;
        cin >> p >> c;
        nodes[i].id = i;
        nodes[i].color = c;
        if (p == 0) root_id = i;
        else nodes[p].children.push_back(&nodes[i]);
    }

    buildDFS(&nodes[root_id]);

    vector<Query> q(n);
    for (int i = 1; i <= n; ++i) {
        q[i - 1] = {nodes[i].tin, nodes[i].tout, i};
    }

    sort(q.begin(), q.end(), compareQueries);

    int current_r = 0;
    for (int i = 0; i < n; ++i) {
        while (current_r < q[i].r) {
            current_r++;
            int node_id = dfs_order[current_r];
            int c = nodes[node_id].color;
            if (last_pos[c]) update(last_pos[c], -1, n);
            update(current_r, 1, n);
            last_pos[c] = current_r;
        }
        result[q[i].id] = query(q[i].r) - query(q[i].l - 1);
    }

    for (int i = 1; i <= n; ++i) {
        cout << result[i] << (i == n ? "" : " ");
    }
    cout << endl;

    return 0;
}

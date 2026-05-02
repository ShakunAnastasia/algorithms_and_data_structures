#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    int max_len;
    int pre_len;
    int suf_len;
    int first_val;
    int last_val;
    int size;
    int lazy_val;
    bool has_lazy;
};

int n, m;
int a[1000005];
Node tree[4000005];

Node merge(const Node& L, const Node& R) {
    Node res;
    res.size = L.size + R.size;
    res.first_val = L.first_val;
    res.last_val = R.last_val;
    res.has_lazy = false;
    res.lazy_val = 0;

    res.max_len = max(L.max_len, R.max_len);
    res.pre_len = L.pre_len;
    res.suf_len = R.suf_len;

    if (L.last_val <= R.first_val) {
        res.max_len = max(res.max_len, L.suf_len + R.pre_len);
        if (L.pre_len == L.size) res.pre_len = L.size + R.pre_len;
        if (R.suf_len == R.size) res.suf_len = R.size + L.suf_len;
    }
    return res;
}

void apply(int v, int val) {
    tree[v].first_val = tree[v].last_val = val;
    tree[v].max_len = tree[v].pre_len = tree[v].suf_len = tree[v].size;
    tree[v].lazy_val = val;
    tree[v].has_lazy = true;
}

void push(int v) {
    if (tree[v].has_lazy) {
        apply(2 * v, tree[v].lazy_val);
        apply(2 * v + 1, tree[v].lazy_val);
        tree[v].has_lazy = false;
    }
}

void build(int v, int tl, int tr) {
    if (tl == tr) {
        tree[v] = {1, 1, 1, a[tl], a[tl], 1, 0, false};
    } else {
        int tm = (tl + tr) / 2;
        build(2 * v, tl, tm);
        build(2 * v + 1, tm + 1, tr);
        tree[v] = merge(tree[2 * v], tree[2 * v + 1]);
    }
}

void update(int v, int tl, int tr, int l, int r, int val) {
    if (l > r) return;
    if (l == tl && r == tr) {
        apply(v, val);
    } else {
        push(v);
        int tm = (tl + tr) / 2;
        update(2 * v, tl, tm, l, min(r, tm), val);
        update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, val);
        tree[v] = merge(tree[2 * v], tree[2 * v + 1]);
    }
}

Node query(int v, int tl, int tr, int l, int r) {
    if (l == tl && r == tr) return tree[v];
    push(v);
    int tm = (tl + tr) / 2;
    if (r <= tm) return query(2 * v, tl, tm, l, r);
    if (l > tm) return query(2 * v + 1, tm + 1, tr, l, r);
    return merge(query(2 * v, tl, tm, l, tm), query(2 * v + 1, tm + 1, tr, tm + 1, r));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; i++) cin >> a[i];
    build(1, 0, n - 1);

    if (!(cin >> m)) return 0;
    while (m--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            cin >> l >> r;
            cout << query(1, 0, n - 1, l - 1, r - 1).max_len << "\n";
        } else {
            int l, r, v;
            cin >> l >> r >> v;
            update(1, 0, n - 1, l - 1, r - 1, v);
        }
    }

    return 0;
}

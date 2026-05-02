#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 500005;
long long tree[4 * MAXN];
int lazy_val[4 * MAXN];
bool has_lazy[4 * MAXN];
int a[MAXN];

void build(int v, int tl, int tr) {
    if (tl == tr) {
        tree[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(2 * v, tl, tm);
        build(2 * v + 1, tm + 1, tr);
        tree[v] = tree[2 * v] + tree[2 * v + 1];
    }
}

void push(int v, int tl, int tr) {
    if (has_lazy[v]) {
        int tm = (tl + tr) / 2;
        
        has_lazy[2 * v] = true;
        lazy_val[2 * v] = lazy_val[v];
        tree[2 * v] = (long long)lazy_val[v] * (tm - tl + 1);
        
        has_lazy[2 * v + 1] = true;
        lazy_val[2 * v + 1] = lazy_val[v];
        tree[2 * v + 1] = (long long)lazy_val[v] * (tr - tm);
        
        has_lazy[v] = false;
    }
}

void update(int v, int tl, int tr, int l, int r, int val) {
    if (l > r) return;
    if (l == tl && r == tr) {
        tree[v] = (long long)val * (tr - tl + 1);
        lazy_val[v] = val;
        has_lazy[v] = true;
    } else {
        push(v, tl, tr);
        int tm = (tl + tr) / 2;
        update(2 * v, tl, tm, l, min(r, tm), val);
        update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, val);
        tree[v] = tree[2 * v] + tree[2 * v + 1];
    }
}

long long query(int v, int tl, int tr, int l, int r) {
    if (l > r) return 0;
    if (l == tl && r == tr) return tree[v];
    push(v, tl, tr);
    int tm = (tl + tr) / 2;
    return query(2 * v, tl, tm, l, min(r, tm)) + 
           query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    for (int i = 1; i <= n; i++) cin >> a[i];
    
    build(1, 1, n);

    while (q--) {
        char type;
        cin >> type;
        if (type == '=') {
            int i, j, d;
            cin >> i >> j >> d;
            if (i > j) swap(i, j);
            update(1, 1, n, i, j, d);
        } else {
            int f, t;
            cin >> f >> t;
            if (f > t) swap(f, t);
            cout << query(1, 1, n, f, t) << "\n";
        }
    }
    return 0;
}

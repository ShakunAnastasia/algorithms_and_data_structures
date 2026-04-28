#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

long long tree[1024];
long long lazy[1024];

void push(int v, int tl, int tr) {
    if (lazy[v] != 0) {
        int tm = (tl + tr) / 2;
        tree[2 * v] += lazy[v] * (tm - tl + 1);
        lazy[2 * v] += lazy[v];
        tree[2 * v + 1] += lazy[v] * (tr - tm);
        lazy[2 * v + 1] += lazy[v];
        lazy[v] = 0;
    }
}

void update(int v, int tl, int tr, int l, int r, int add) {
    if (l > r) return;
    if (l == tl && r == tr) {
        tree[v] += (long long)add * (tr - tl + 1);
        lazy[v] += add;
    } else {
        push(v, tl, tr);
        int tm = (tl + tr) / 2;
        update(2 * v, tl, tm, l, min(r, tm), add);
        update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add);
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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int q, p;
    long long L, R;
    cin >> q >> L >> R >> p;

    for (int i = 0; i < q; ++i) {
        int qL = min(L, R);
        int qR = max(L, R);
        
        update(1, 0, 255, qL, qR, 1);
        
        if (i < q - 1) {
            long long s = query(1, 0, 255, qL, qR);
            L = s % p;
            R = 255 - (s % p);
        }
    }

    cout << query(1, 0, 255, 0, 255) << endl;

    return 0;
}

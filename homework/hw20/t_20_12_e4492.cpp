#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 1000005;
int tree[4 * MAXN];
int n;

void build(const vector<int>& a, int v, int tl, int tr) {
    if (tl == tr) {
        tree[v] = a[tl - 1];
    } else {
        int tm = (tl + tr) / 2;
        build(a, 2 * v, tl, tm);
        build(a, 2 * v + 1, tm + 1, tr);
        tree[v] = max(tree[2 * v], tree[2 * v + 1]);
    }
}

void update(int v, int tl, int tr, int pos, int val) {
    if (tl == tr) {
        tree[v] = val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(2 * v, tl, tm, pos, val);
        else
            update(2 * v + 1, tm + 1, tr, pos, val);
        tree[v] = max(tree[2 * v], tree[2 * v + 1]);
    }
}

int find_first_exact(int v, int tl, int tr, int p) {
    if (tree[v] < p) return -1;
    if (tl == tr) return (tree[v] == p ? tl : -1);
    int tm = (tl + tr) / 2;
    int res = find_first_exact(2 * v, tl, tm, p);
    if (res != -1) return res;
    return find_first_exact(2 * v + 1, tm + 1, tr, p);
}

int find_last_greater(int v, int tl, int tr, int l, int r, int p) {
    if (tl > r || tr < l || tree[v] <= p) return -1;
    if (tl == tr) return tl;
    int tm = (tl + tr) / 2;
    int res = find_last_greater(2 * v + 1, tm + 1, tr, l, r, p);
    if (res != -1) return res;
    return find_last_greater(2 * v, tl, tm, l, r, p);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    build(a, 1, 1, n);

    int m;
    cin >> m;
    while (m--) {
        int type;
        cin >> type;
        if (type == 1) {
            int p;
            cin >> p;
            int k = find_first_exact(1, 1, n, p);
            if (k == -1) {
                cout << "Error" << "\n";
            } else {
                int last_g = (k == 1) ? -1 : find_last_greater(1, 1, n, 1, k - 1, p);
                int l = (last_g == -1) ? 1 : last_g + 1;
                cout << l << " " << k << "\n";
            }
        } else {
            int x, y;
            cin >> x >> y;
            update(1, 1, n, x, y);
        }
    }

    return 0;
}

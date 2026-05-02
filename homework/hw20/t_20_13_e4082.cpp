#include <iostream>
#include <vector>
#include <string>

using namespace std;

int get_sign(int v) {
    if (v > 0) return 1;
    if (v < 0) return -1;
    return 0;
}

void build(vector<int>& tree, const vector<int>& a, int v, int tl, int tr) {
    if (tl == tr) {
        tree[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(tree, a, 2 * v, tl, tm);
        build(tree, a, 2 * v + 1, tm + 1, tr);
        tree[v] = tree[2 * v] * tree[2 * v + 1];
    }
}

void update(vector<int>& tree, int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        tree[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(tree, 2 * v, tl, tm, pos, new_val);
        else
            update(tree, 2 * v + 1, tm + 1, tr, pos, new_val);
        tree[v] = tree[2 * v] * tree[2 * v + 1];
    }
}

int query(vector<int>& tree, int v, int tl, int tr, int l, int r) {
    if (l > r) return 1;
    if (l == tl && r == tr) return tree[v];
    int tm = (tl + tr) / 2;
    return query(tree, 2 * v, tl, tm, l, min(r, tm)) *
           query(tree, 2 * v + 1, tm + 1, tr, max(l, tm + 1), r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    while (cin >> n >> k) {
        vector<int> a(n + 1);
        for (int i = 1; i <= n; i++) {
            int x;
            cin >> x;
            a[i] = get_sign(x);
        }

        vector<int> tree(4 * n + 1);
        build(tree, a, 1, 1, n);

        string result = "";
        for (int q = 0; q < k; q++) {
            char type;
            cin >> type;
            if (type == 'C') {
                int i, v;
                cin >> i >> v;
                update(tree, 1, 1, n, i, get_sign(v));
            } else {
                int i, j;
                cin >> i >> j;
                int res = query(tree, 1, 1, n, i, j);
                if (res > 0) result += '+';
                else if (res < 0) result += '-';
                else result += '0';
            }
        }
        cout << result << "\n";
    }
    return 0;
}

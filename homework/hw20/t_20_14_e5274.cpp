#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

const ll MOD = 1e9 + 9;
const ll P = 131;

ll p_pow[100005];
ll tree[400005];
int n, k;
string s;

void build(int v, int tl, int tr) {
    if (tl == tr) {
        tree[v] = s[tl - 1];
    } else {
        int tm = (tl + tr) / 2;
        build(2 * v, tl, tm);
        build(2 * v + 1, tm + 1, tr);
        tree[v] = (tree[2 * v] * p_pow[tr - tm] + tree[2 * v + 1]) % MOD;
    }
}

void update(int v, int tl, int tr, int pos, char c) {
    if (tl == tr) {
        tree[v] = c;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(2 * v, tl, tm, pos, c);
        else
            update(2 * v + 1, tm + 1, tr, pos, c);
        tree[v] = (tree[2 * v] * p_pow[tr - tm] + tree[2 * v + 1]) % MOD;
    }
}

ll query(int v, int tl, int tr, int l, int r) {
    if (l > r) return 0;
    if (l == tl && r == tr) return tree[v];
    int tm = (tl + tr) / 2;
    ll left_h = query(2 * v, tl, tm, l, min(r, tm));
    ll right_h = query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r);
    int right_len = max(0, min(r, tr) - max(l, tm + 1) + 1);
    return (left_h * p_pow[right_len] + right_h) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> k)) return 0;
    cin >> s;

    p_pow[0] = 1;
    for (int i = 1; i <= n; i++)
        p_pow[i] = (p_pow[i - 1] * P) % MOD;

    build(1, 1, n);

    while (k--) {
        char type;
        cin >> type;
        if (type == '*') {
            int i;
            char c;
            cin >> i >> c;
            update(1, 1, n, i, c);
        } else {
            int i, j, len;
            cin >> i >> j >> len;
            if (query(1, 1, n, i, i + len - 1) == query(1, 1, n, j, j + len - 1))
                cout << "+";
            else
                cout << "-";
        }
    }
    cout << endl;

    return 0;
}

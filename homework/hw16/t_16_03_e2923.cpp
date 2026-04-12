#include <cstdio>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

const int MAXN = 1000005;
vector<int> adj[MAXN];
int col[MAXN], tin[MAXN], tout[MAXN], timer, order[MAXN];
int bit[MAXN], last_pos[MAXN], res[MAXN];

struct Query {
    int l, r, id;
};

void update(int i, int val, int n) {
    for (; i <= n; i += i & -i) bit[i] += val;
}

int get_sum(int i) {
    int s = 0;
    for (; i > 0; i -= i & -i) s += bit[i];
    return s;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    int root = -1;
    for (int i = 1; i <= n; ++i) {
        int p, c;
        scanf("%d %d", &p, &c);
        col[i] = c;
        if (p == 0) root = i;
        else adj[p].push_back(i);
    }

    stack<pair<int, int>> st;
    st.push({root, 0});
    while (!st.empty()) {
        int u = st.top().first;
        int &idx = st.top().second;
        if (idx == 0) {
            tin[u] = ++timer;
            order[timer] = u;
        }
        if (idx < adj[u].size()) {
            st.push({adj[u][idx++], 0});
        } else {
            tout[u] = timer;
            st.pop();
        }
    }

    vector<Query> q(n);
    for (int i = 1; i <= n; ++i) {
        q[i - 1] = {tin[i], tout[i], i};
    }

    sort(q.begin(), q.end(), [](const Query& a, const Query& b) {
        return a.r < b.r;
    });

    int curr_r = 0;
    for (int i = 0; i < n; ++i) {
        while (curr_r < q[i].r) {
            curr_r++;
            int u = order[curr_r];
            int c = col[u];
            if (last_pos[c]) {
                update(last_pos[c], -1, n);
            }
            update(curr_r, 1, n);
            last_pos[c] = curr_r;
        }
        res[q[i].id] = get_sum(q[i].r) - get_sum(q[i].l - 1);
    }

    for (int i = 1; i <= n; ++i) {
        printf("%d%c", res[i], (i == n ? '\n' : ' '));
    }

    return 0;
}

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
bool visited[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<vector<int>> components;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            vector<int> current_comp;
            queue<int> q;
            
            q.push(i);
            visited[i] = true;
            
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                current_comp.push_back(u);
                
                for (int v : adj[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        q.push(v);
                    }
                }
            }
            components.push_back(current_comp);
        }
    }

    cout << components.size() << "\n";
    for (const auto& comp : components) {
        cout << comp.size() << "\n";
        for (int i = 0; i < comp.size(); ++i) {
            cout << comp[i] << (i == comp.size() - 1 ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}

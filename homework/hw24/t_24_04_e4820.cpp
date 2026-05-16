#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int dist[1005][1005];
char grid[1005][1005];
int dr[] = {0, 0, 1, -1};
int dc[] = {1, -1, 0, 0};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grid[i][j];
            dist[i][j] = -1;
        }
    }

    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    int start_r = y1 - 1;
    int start_c = x1 - 1;
    int end_r = y2 - 1;
    int end_c = x2 - 1;

    if (grid[start_r][start_c] == '1' || grid[end_r][end_c] == '1') {
        cout << -1 << endl;
        return 0;
    }

    queue<pair<int, int>> q;
    q.push({start_r, start_c});
    dist[start_r][start_c] = 0;

    while (!q.empty()) {
        pair<int, int> curr = q.front();
        q.pop();

        int r = curr.first;
        int c = curr.second;

        if (r == end_r && c == end_c) {
            cout << dist[r][c] << endl;
            return 0;
        }

        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                if (grid[nr][nc] == '0' && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    q.push({nr, nc});
                }
            }
        }
    }

    cout << -1 << endl;
    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

bool grid[105][105];
int dr[] = {0, 0, 1, -1};
int dc[] = {1, -1, 0, 0};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<pair<int, int>> flooded;
    for (int i = 0; i < k; ++i) {
        int r, c;
        cin >> r >> c;
        grid[r][c] = true;
        flooded.push_back({r, c});
    }

    int max_lake = 0;
    for (auto& start : flooded) {
        if (grid[start.first][start.second]) {
            int current_size = 0;
            stack<pair<int, int>> s;
            
            s.push(start);
            grid[start.first][start.second] = false;

            while (!s.empty()) {
                pair<int, int> curr = s.top();
                s.pop();
                current_size++;

                for (int i = 0; i < 4; ++i) {
                    int nr = curr.first + dr[i];
                    int nc = curr.second + dc[i];

                    if (nr >= 1 && nr <= n && nc >= 1 && nc <= m) {
                        if (grid[nr][nc]) {
                            grid[nr][nc] = false;
                            s.push({nr, nc});
                        }
                    }
                }
            }
            if (current_size > max_lake) {
                max_lake = current_size;
            }
        }
    }

    cout << max_lake << endl;

    return 0;
}

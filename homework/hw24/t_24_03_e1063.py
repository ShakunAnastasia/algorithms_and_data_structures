import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    m = int(data[0])
    n = int(data[1])
    grid = data[2:]
    
    visited = [[False for _ in range(n)] for _ in range(m)]
    count = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                count += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            if grid[nr][nc] == '#' and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                                
    print(count)

if __name__ == "__main__":
    solve()

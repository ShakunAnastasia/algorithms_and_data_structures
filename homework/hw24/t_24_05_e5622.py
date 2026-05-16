import sys
from collections import deque

def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    
    if grid[0][0] == '.':
        queue.append((0, 0))
        visited[0][0] = True
    if grid[n-1][n-1] == '.' and not visited[n-1][n-1]:
        queue.append((n-1, n-1))
        visited[n-1][n-1] = True
        
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and grid[nr][nc] == '.':
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    
    faces = 0
    for r in range(n):
        for c in range(n):
            if visited[r][c]:
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == '#':
                            faces += 1
                    else:
                        if (r == 0 and c == 0) and (nr == -1 or nc == -1):
                            continue
                        if (r == n - 1 and c == n - 1) and (nr == n or nc == n):
                            continue
                        faces += 1
                            
    print(faces * 9)

if __name__ == "__main__":
    solve()

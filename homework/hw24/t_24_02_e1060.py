import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    grid = [list(row) for row in data[1:]]
    
    start_pos = None
    end_pos = None
    
    for r in range(n):
        for c in range(n):
            if grid[r][c] == '@':
                start_pos = (r, c)
            elif grid[r][c] == 'X':
                end_pos = (r, c)
    
    queue = deque([start_pos])
    parent = {start_pos: None}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    found = False
    
    while queue:
        r, c = queue.popleft()
        if (r, c) == end_pos:
            found = True
            break
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if (nr, nc) not in parent:
                    if grid[nr][nc] == '.' or grid[nr][nc] == 'X':
                        parent[(nr, nc)] = (r, c)
                        queue.append((nr, nc))
    
    if found:
        print("Y")
        curr = end_pos
        while curr is not None:
            r, c = curr
            if grid[r][c] == 'X' or grid[r][c] == '.':
                grid[r][c] = '+'
            curr = parent[curr]
            
        for row in grid:
            print("".join(row))
    else:
        print("N")

if __name__ == "__main__":
    solve()

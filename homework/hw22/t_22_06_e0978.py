import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        
    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])
    
    count = 0
    while queue and count < n - 1:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                sys.stdout.write(f"{u} {v}\n")
                queue.append(v)
                count += 1

if __name__ == "__main__":
    solve()

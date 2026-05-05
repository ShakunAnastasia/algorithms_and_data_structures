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
        
    k = int(next(it))
    dist = [-1] * (n + 1)
    queue = deque()
    
    for _ in range(k):
        s = int(next(it))
        dist[s] = 0
        queue.append(s)
        
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    
    max_t = -1
    best_v = -1
    for i in range(1, n + 1):
        if dist[i] > max_t:
            max_t = dist[i]
            best_v = i
        elif dist[i] == max_t:
            if best_v == -1 or i < best_v:
                best_v = i
    
    sys.stdout.write(f"{max_t}\n{best_v}\n")

if __name__ == "__main__":
    solve()

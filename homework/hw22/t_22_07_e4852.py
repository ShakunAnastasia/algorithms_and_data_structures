import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    x = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            val = next(it)
            if val == "1":
                adj[i].append(j)
                
    dist = [-1] * (n + 1)
    dist[x] = 0
    queue = deque([x])
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
                
    print(*(dist[1:]))

if __name__ == "__main__":
    solve()

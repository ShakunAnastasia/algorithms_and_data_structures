import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    color = [-1] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
                        
    print("YES")

if __name__ == "__main__":
    solve()

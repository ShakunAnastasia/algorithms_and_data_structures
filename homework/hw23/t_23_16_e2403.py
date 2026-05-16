import sys

sys.setrecursionlimit(2000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    rev = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        rev[v].append(u)

    visited = [False] * (n + 1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    def dfs2(u):
        visited[u] = True
        for v in rev[u]:
            if not visited[v]:
                dfs2(v)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)

    visited = [False] * (n + 1)
    count = 0
    for i in reversed(order):
        if not visited[i]:
            count += 1
            dfs2(i)
    
    print(count)

if __name__ == "__main__":
    solve()

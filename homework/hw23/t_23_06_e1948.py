import sys

sys.setrecursionlimit(200000)

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
        
    visited = [0] * (n + 1)
    result = []
    has_cycle = False
    
    def dfs(u):
        nonlocal has_cycle
        visited[u] = 1
        for v in adj[u]:
            if visited[v] == 1:
                has_cycle = True
                return
            if visited[v] == 0:
                dfs(v)
                if has_cycle:
                    return
        visited[u] = 2
        result.append(u)

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
            if has_cycle:
                break
                
    if has_cycle:
        print("-1")
    else:
        print(*(result[::-1]))

if __name__ == "__main__":
    solve()

import sys

sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        
    match = [-1] * (n + 1)
    vis = [0] * (n + 1)

    def dfs(u, token):
        for v in adj[u]:
            if vis[v] != token:
                vis[v] = token
                if match[v] < 0 or dfs(match[v], token):
                    match[v] = u
                    return True
        return False

    matching_size = 0
    for i in range(1, n + 1):
        if dfs(i, i):
            matching_size += 1
            
    print(n - matching_size)

if __name__ == "__main__":
    solve()

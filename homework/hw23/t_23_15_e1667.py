import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        rev_adj[v].append(u)
        
    visited = [False] * (n + 1)
    stack = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs_stack = [(i, 0)]
            while dfs_stack:
                u, edge_idx = dfs_stack.pop()
                if edge_idx == 0:
                    if visited[u]: continue
                    visited[u] = True
                
                if edge_idx < len(adj[u]):
                    dfs_stack.append((u, edge_idx + 1))
                    v = adj[u][edge_idx]
                    if not visited[v]:
                        dfs_stack.append((v, 0))
                else:
                    stack.append(u)
                    
    scc_id = [0] * (n + 1)
    scc_count = 0
    
    for i in reversed(stack):
        if scc_id[i] == 0:
            scc_count += 1
            dfs_stack = [i]
            scc_id[i] = scc_count
            while dfs_stack:
                u = dfs_stack.pop()
                for v in rev_adj[u]:
                    if scc_id[v] == 0:
                        scc_id[v] = scc_count
                        dfs_stack.append(v)
                        
    print(scc_count)
    print(*(scc_id[1:]))

if __name__ == "__main__":
    solve()

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
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        rev_adj[v].append(u)
        edges.append((u, v))
        
    order = []
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                u, idx = stack.pop()
                if idx == 0:
                    if visited[u]: continue
                    visited[u] = True
                if idx < len(adj[u]):
                    stack.append((u, idx + 1))
                    v = adj[u][idx]
                    if not visited[v]:
                        stack.append((v, 0))
                else:
                    order.append(u)
                    
    scc = [-1] * (n + 1)
    scc_count = 0
    for i in reversed(order):
        if scc[i] == -1:
            stack = [i]
            scc[i] = scc_count
            while stack:
                u = stack.pop()
                for v in rev_adj[u]:
                    if scc[v] == -1:
                        scc[v] = scc_count
                        stack.append(v)
            scc_count += 1
            
    cond_edges = set()
    for u, v in edges:
        root_u = scc[u]
        root_v = scc[v]
        if root_u != root_v:
            cond_edges.add((root_u, root_v))
            
    print(len(cond_edges))

if __name__ == "__main__":
    solve()

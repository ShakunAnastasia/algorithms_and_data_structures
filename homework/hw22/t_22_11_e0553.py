import sys
from collections import deque

def solve():
    raw_data = sys.stdin.read().split()
    if not raw_data:
        return
    
    n = int(raw_data[0])
    idx = 1
    proc_names = []
    adj_temp = {}
    
    for _ in range(n):
        while idx < len(raw_data) and raw_data[idx] == "*****":
            idx += 1
        if idx >= len(raw_data):
            break
            
        name = raw_data[idx]
        proc_names.append(name)
        idx += 1
        
        k = int(raw_data[idx])
        idx += 1
        
        calls = []
        for _ in range(k):
            calls.append(raw_data[idx])
            idx += 1
        adj_temp[name] = calls
        
    name_to_id = {name: i for i, name in enumerate(proc_names)}
    adj = [[] for _ in range(n)]
    for name in proc_names:
        u = name_to_id[name]
        for called_name in adj_temp[name]:
            v = name_to_id[called_name]
            adj[u].append(v)
            
    for i in range(n):
        queue = deque([i])
        visited = [False] * n
        found = False
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v == i:
                    found = True
                    break
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
            if found:
                break
        
        result = "YES" if found else "NO"
        sys.stdout.write(f"{proc_names[i]}: {result}\n")

if __name__ == "__main__":
    solve()

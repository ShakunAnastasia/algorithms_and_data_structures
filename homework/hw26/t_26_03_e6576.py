import sys
from collections import deque

def solve_test_case(data, start_idx):
    n = int(data[start_idx])
    m = int(data[start_idx + 1])
    p = int(data[start_idx + 2]) - 1
    q = int(data[start_idx + 3]) - 1
    
    idx = start_idx + 4
    
    target_weight = None
    edges = []
    
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        idx += 3
        
        if (u == p and v == q) or (u == q and v == p):
            target_weight = w
        else:
            edges.append((u, v, w))
            
    if target_weight is None:
        print("NO")
        return idx
        
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        if w < target_weight:
            adj[u].append(v)
            adj[v].append(u)
            
    visited = [False] * n
    visited[p] = True
    queue = deque([p])
    
    path_exists_via_smaller = False
    
    while queue:
        curr = queue.popleft()
        if curr == q:
            path_exists_via_smaller = True
            break
            
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
    if path_exists_via_smaller:
        print("NO")
    else:
        print("YES")
        
    return idx

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t_tests = int(input_data[0])
    current_index = 1
    
    for _ in range(t_tests):
        current_index = solve_test_case(input_data, current_index)

if __name__ == "__main__":
    main()

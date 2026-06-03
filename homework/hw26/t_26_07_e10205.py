import sys
import math

def solve_test(input_data, idx, is_first):
    if idx >= len(input_data):
        return idx
        
    n = int(input_data[idx])
    idx += 1
    
    coords = []
    for _ in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        idx += 2
        coords.append((x, y))
        
    m = int(input_data[idx])
    idx += 1
    
    prebuilt = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        prebuilt[u].append(v)
        prebuilt[v].append(u)
        
    if not is_first:
        print()
        
    inf = float('inf')
    min_dist = [inf] * n
    parent = [-1] * n
    visited = [False] * n
    
    min_dist[0] = 0
    new_highways = []
    
    for _ in range(n):
        u = -1
        current_min = inf
        for i in range(n):
            if not visited[i] and min_dist[i] < current_min:
                current_min = min_dist[i]
                u = i
                
        visited[u] = True
        
        if current_min > 0 and parent[u] != -1:
            ux, uy = coords[u]
            px, py = coords[parent[u]]
            actual_dist = math.sqrt((ux - px) ** 2 + (uy - py) ** 2)
            if abs(current_min - actual_dist) < 1e-9:
                new_highways.append((min(u, parent[u]) + 1, max(u, parent[u]) + 1))
                
        ux, uy = coords[u]
        
        for neighbor in prebuilt[u]:
            if not visited[neighbor] and 0 < min_dist[neighbor]:
                min_dist[neighbor] = 0
                parent[neighbor] = u
                
        for v in range(n):
            if not visited[v]:
                vx, vy = coords[v]
                dist = math.sqrt((ux - vx) ** 2 + (uy - vy) ** 2)
                if dist < min_dist[v]:
                    min_dist[v] = dist
                    parent[v] = u
                    
    if not new_highways:
        print("No new highways need")
    else:
        for u, v in new_highways:
            print(u, v)
            
    return idx

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t_tests = int(input_data[0])
    current_idx = 1
    
    for i in range(t_tests):
        current_idx = solve_test(input_data, current_idx, i == 0)

if __name__ == "__main__":
    main()

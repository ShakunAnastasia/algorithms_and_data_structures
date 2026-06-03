import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        if n == 0:
            break
            
        coords = []
        for _ in range(n):
            x = int(input_data[idx])
            y = int(input_data[idx + 1])
            idx += 2
            coords.append((x, y))
            
        inf = float('inf')
        min_dist = [inf] * n
        visited = [False] * n
        
        min_dist[0] = 0
        total_length = 0.0
        
        for _ in range(n):
            u = -1
            current_min = inf
            for i in range(n):
                if not visited[i] and min_dist[i] < current_min:
                    current_min = min_dist[i]
                    u = i
                    
            visited[u] = True
            total_length += current_min
            
            ux, uy = coords[u]
            
            for v in range(n):
                if not visited[v]:
                    vx, vy = coords[v]
                    dist = math.sqrt((ux - vx) ** 2 + (uy - vy) ** 2)
                    if dist < min_dist[v]:
                        min_dist[v] = dist
                        
        print(f"{total_length:.2f}")

if __name__ == "__main__":
    solve()

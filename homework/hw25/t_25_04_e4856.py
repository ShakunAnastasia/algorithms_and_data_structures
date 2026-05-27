import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2]) - 1
    f = int(input_data[3]) - 1
    
    adj = [[] for _ in range(n)]
    idx = 4
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    inf = float('inf')
    distances = [inf] * n
    parent = [-1] * n
    distances[s] = 0
    
    pq = [(0, s)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > distances[u]:
            continue
            
        if u == f:
            break
            
        for v, weight in adj[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parent[v] = u
                heapq.heappush(pq, (distances[v], v))
                
    if distances[f] == inf:
        print(-1)
    else:
        print(distances[f])
        path = []
        curr = f
        while curr != -1:
            path.append(curr + 1)
            curr = parent[curr]
        print(*(path[::-1]))

if __name__ == "__main__":
    main()

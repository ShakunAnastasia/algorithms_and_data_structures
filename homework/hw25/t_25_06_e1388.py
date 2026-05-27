import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    costs = [int(x) for x in input_data[1 : n + 1]]
    
    m = int(input_data[n + 1])
    
    adj = [[] for _ in range(n)]
    idx = n + 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u].append((v, costs[u]))
        adj[v].append((u, costs[v]))
        
    inf = float('inf')
    distances = [inf] * n
    distances[0] = 0
    
    pq = [(0, 0)]
    
    while pq:
        current_cost, u = heapq.heappop(pq)
        
        if current_cost > distances[u]:
            continue
            
        if u == n - 1:
            break
            
        for v, weight in adj[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))
                
    if distances[n - 1] == inf:
        print(-1)
    else:
        print(distances[n - 1])

if __name__ == "__main__":
    main()

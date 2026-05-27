import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    s = int(input_data[1]) - 1
    f = int(input_data[2]) - 1
    
    matrix = []
    idx = 3
    for _ in range(n):
        row = [int(x) for x in input_data[idx : idx + n]]
        matrix.append(row)
        idx += n
        
    inf = float('inf')
    distances = [inf] * n
    distances[s] = 0
    
    pq = [(0, s)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > distances[u]:
            continue
            
        if u == f:
            break
            
        for v in range(n):
            weight = matrix[u][v]
            if weight != -1:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(pq, (distances[v], v))
                    
    if distances[f] == inf:
        print(-1)
    else:
        print(distances[f])

if __name__ == "__main__":
    main()

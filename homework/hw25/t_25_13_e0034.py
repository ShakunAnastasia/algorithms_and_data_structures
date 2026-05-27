import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m_prizes = int(input_data[1])
    k_edges = int(input_data[2])
    
    winners = [int(x) - 1 for x in input_data[3 : 3 + m_prizes]]
    
    idx = 3 + m_prizes
    adj = [[] for _ in range(n)]
    for _ in range(k_edges):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    sponsor_start = int(input_data[idx]) - 1
    
    inf = float('inf')
    distances = [inf] * n
    distances[sponsor_start] = 0
    
    pq = [(0, sponsor_start)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > distances[u]:
            continue
            
        for v, weight in adj[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))
                
    max_time = 0
    possible = True
    
    for winner in winners:
        if distances[winner] == inf:
            possible = False
            break
        if distances[winner] > max_time:
            max_time = distances[winner]
            
    if possible:
        print("The good sponsor!")
        print(max_time)
    else:
        print("It is not fault of sponsor...")

if __name__ == "__main__":
    main()

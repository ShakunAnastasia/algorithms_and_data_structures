import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    d = int(input_data[1]) - 1
    v_target = int(input_data[2]) - 1
    r_flights = int(input_data[3])
    
    adj = [[] for _ in range(n)]
    idx = 4
    for _ in range(r_flights):
        from_village = int(input_data[idx]) - 1
        t_start = int(input_data[idx + 1])
        to_village = int(input_data[idx + 2]) - 1
        t_end = int(input_data[idx + 3])
        idx += 4
        adj[from_village].append((t_start, to_village, t_end))
        
    inf = float('inf')
    arrival_time = [inf] * n
    arrival_time[d] = 0
    
    pq = [(0, d)]
    
    while pq:
        current_time, u = heapq.heappop(pq)
        
        if current_time > arrival_time[u]:
            continue
            
        if u == v_target:
            break
            
        for t_start, v, t_end in adj[u]:
            if arrival_time[u] <= t_start:
                if t_end < arrival_time[v]:
                    arrival_time[v] = t_end
                    heapq.heappush(pq, (t_end, v))
                    
    if arrival_time[v_target] == inf:
        print(-1)
    else:
        print(arrival_time[v_target])

if __name__ == "__main__":
    main()

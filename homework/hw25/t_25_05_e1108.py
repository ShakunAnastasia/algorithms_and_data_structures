import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        idx += 3
        edges.append((u, v, w))
        
    inf = float('inf')
    distances = [inf] * n
    distances[0] = 0
    
    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] != inf and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                
    has_negative_cycle = False
    for u, v, w in edges:
        if distances[u] != inf and distances[u] + w < distances[v]:
            has_negative_cycle = True
            break
            
    if has_negative_cycle:
        print("possible")
    else:
        print("not possible")

if __name__ == "__main__":
    main()

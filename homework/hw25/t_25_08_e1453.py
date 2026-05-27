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
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        edges.append((u, v, w))
        
    inf = float('inf')
    distances = [inf] * n
    distances[0] = 0
    
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if distances[u] != inf and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                changed = True
        if not changed:
            break
            
    result = []
    for d in distances:
        if d == inf:
            result.append(30000)
        else:
            result.append(d)
            
    print(*(result))

if __name__ == "__main__":
    main()

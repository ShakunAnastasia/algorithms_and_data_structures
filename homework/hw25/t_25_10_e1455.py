import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    edges = []
    idx = 1
    for i in range(n):
        for j in range(n):
            val = int(input_data[idx])
            idx += 1
            if val != 100000:
                edges.append((i, j, val))
                
    distances = [0] * n
    parent = [-1] * n
    
    start_vertex_in_cycle = -1
    
    for iteration in range(n):
        start_vertex_in_cycle = -1
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                parent[v] = u
                start_vertex_in_cycle = v
                
    if start_vertex_in_cycle == -1:
        print("NO")
    else:
        print("YES")
        
        curr = start_vertex_in_cycle
        for _ in range(n):
            curr = parent[curr]
            
        cycle = []
        node = curr
        while True:
            cycle.append(node)
            if node == curr and len(cycle) > 1:
                break
            node = parent[node]
            
        cycle = cycle[::-1]
        
        print(len(cycle))
        print(*(v + 1 for v in cycle))

if __name__ == "__main__":
    main()

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges_seen = set()
    ptr = 2
    
    has_multi_edge = False
    for _ in range(m):
        if ptr + 1 >= len(input_data):
            break
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        
        edge = (u, v)
        if edge in edges_seen:
            has_multi_edge = True
            break
        edges_seen.add(edge)
        ptr += 2
        
    if has_multi_edge:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()

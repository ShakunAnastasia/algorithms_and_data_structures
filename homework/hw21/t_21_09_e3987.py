import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    if n == 1:
        print("YES")
        return
        
    unique_edges = set()
    ptr = 2
    for _ in range(m):
        if ptr + 1 >= len(input_data):
            break
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        
        if u != v:
            if u > v:
                u, v = v, u
            unique_edges.add((u, v))
        ptr += 2
        
    if len(unique_edges) == n * (n - 1) // 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()

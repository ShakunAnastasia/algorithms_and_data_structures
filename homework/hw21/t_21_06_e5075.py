import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)
    
    ptr = 2
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        out_degree[u] += 1
        in_degree[v] += 1
        ptr += 2
        
    for i in range(1, n + 1):
        sys.stdout.write(f"{in_degree[i]} {out_degree[i]}\n")

if __name__ == "__main__":
    solve()

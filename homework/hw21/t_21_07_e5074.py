import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    degrees = [0] * (n + 1)
    
    ptr = 2
    for _ in range(m):
        if ptr + 1 >= len(data):
            break
        u = int(data[ptr])
        v = int(data[ptr + 1])
        degrees[u] += 1
        degrees[v] += 1
        ptr += 2
        
    print(*degrees[1:], sep='\n')

if __name__ == "__main__":
    solve()

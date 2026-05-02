import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    ptr = 1
    hanging_vertices = 0
    
    for i in range(n):
        degree = 0
        for j in range(n):
            degree += int(data[ptr])
            ptr += 1
        if degree == 1:
            hanging_vertices += 1
            
    print(hanging_vertices)

if __name__ == "__main__":
    solve()

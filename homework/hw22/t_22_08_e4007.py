import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    start_str = data[0]
    end_str = data[1]
    
    start = int(start_str)
    target = int(end_str)
    
    if start == target:
        print(start)
        return

    parent = {}
    queue = deque([start_str])
    parent[start_str] = None
    
    while queue:
        curr = queue.popleft()
        
        if curr == end_str:
            path = []
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            print(*(path[::-1]), sep='\n')
            return
        
        d1, d2, d3, d4 = map(int, list(curr))
        
        neighbors = []
        
        if d1 < 9:
            neighbors.append(str(d1 + 1) + curr[1:])
            
        if d4 > 1:
            neighbors.append(curr[:3] + str(d4 - 1))
            
        neighbors.append(curr[3] + curr[0:3])
        
        neighbors.append(curr[1:4] + curr[0])
        
        for nxt in neighbors:
            if nxt not in parent:
                parent[nxt] = curr
                queue.append(nxt)

if __name__ == "__main__":
    solve()

import sys

def is_strongly_connected(matrix, n):
    if n <= 1:
        return True
    
    visited = [False] * n
    stack = [0]
    visited[0] = True
    count = 1
    while stack:
        u = stack.pop()
        for v in range(n):
            if matrix[u][v] and not visited[v]:
                visited[v] = True
                count += 1
                stack.append(v)
    if count != n:
        return False
    
    visited = [False] * n
    stack = [0]
    visited[0] = True
    count = 1
    while stack:
        u = stack.pop()
        for v in range(n):
            if matrix[v][u] and not visited[v]:
                visited[v] = True
                count += 1
                stack.append(v)
    return count == n

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    n = int(next(it))
    adj = [[0] * n for _ in range(n)]
    
    for i in range(n):
        m_count = int(next(it))
        for _ in range(m_count):
            src = int(next(it)) - 1
            adj[src][i] = 1
            
    for i in range(n):
        for j in range(i + 1, n):
            if adj[i][j] == 0 and adj[j][i] == 0:
                adj[i][j] = 1

    for x in range(n):
        new_adj = [row[:] for row in adj]
        for j in range(n):
            if x != j:
                new_adj[x][j], new_adj[j][x] = new_adj[j][x], new_adj[x][j]
        
        if is_strongly_connected(new_adj, n):
            print(1)
            return
            
    print(0)

if __name__ == '__main__':
    solve()

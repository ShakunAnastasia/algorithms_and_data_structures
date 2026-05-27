import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    k_roads = int(input_data[1])
    
    inf = float('inf')
    matrix = [[inf] * n for _ in range(n)]
    
    for i in range(n):
        matrix[i][i] = 0
        
    idx = 2
    for _ in range(k_roads):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        if w < matrix[u][v]:
            matrix[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    total_sum = 0
    pairs_count = 0
    
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != inf:
                total_sum += matrix[i][j]
                pairs_count += 1

    if pairs_count == 0:
        print(f"{0.0:0.6f}")
    else:
        average = total_sum / pairs_count
        print(f"{average:0.6f}")

if __name__ == "__main__":
    main()

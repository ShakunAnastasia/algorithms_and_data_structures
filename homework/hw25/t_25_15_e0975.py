import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    inf = float('inf')
    matrix = []
    idx = 1
    
    for _ in range(n):
        row = []
        for x in input_data[idx : idx + n]:
            val = int(x)
            if val == -1:
                row.append(inf)
            else:
                row.append(val)
        matrix.append(row)
        idx += n

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    max_dist = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != inf and matrix[i][j] > max_dist:
                max_dist = matrix[i][j]

    print(max_dist)

if __name__ == "__main__":
    main()

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    inf = float('inf')
    matrix = []
    idx = 1
    
    for i in range(n):
        row = []
        for j in range(n):
            val = int(input_data[idx])
            idx += 1
            if i == j:
                if val < 0:
                    row.append(val)
                else:
                    row.append(0)
            elif val == 0:
                row.append(inf)
            else:
                row.append(val)
        matrix.append(row)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] != inf and matrix[k][j] != inf:
                    if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]

    result = [[1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == inf:
                result[i][j] = 0

    for k in range(n):
        if matrix[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != inf and matrix[k][j] != inf:
                        result[i][j] = 2

    for row in result:
        print(*(row))

if __name__ == "__main__":
    main()

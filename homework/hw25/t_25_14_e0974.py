import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    matrix = []
    idx = 1
    for _ in range(n):
        row = [int(x) for x in input_data[idx : idx + n]]
        matrix.append(row)
        idx += n

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    for row in matrix:
        print(*(row))

if __name__ == "__main__":
    main()

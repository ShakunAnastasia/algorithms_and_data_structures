import sys

sys.setrecursionlimit(200000)

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    robots = []
    for k in range(n):
        primary = int(input_data[1 + 2*k])
        auxiliary = int(input_data[2 + 2*k])
        robots.append([primary, auxiliary])
        
    merge_sort(robots)
    
    output = []
    for r in robots:
        output.append(f"{r[0]} {r[1]}")
    
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

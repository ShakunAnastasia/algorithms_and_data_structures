import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])
    
    tree_min = [0] * (2 * n)
    tree_max = [0] * (2 * n)
    
    for i in range(n):
        tree_min[n + i] = a[i]
        tree_max[n + i] = a[i]
        
    for i in range(n - 1, 0, -1):
        tree_min[i] = min(tree_min[2 * i], tree_min[2 * i + 1])
        tree_max[i] = max(tree_max[2 * i], tree_max[2 * i + 1])
        
    ptr = n + 2
    results = []
    
    for _ in range(m):
        q = int(input_data[ptr])
        l = int(input_data[ptr+1])
        r = int(input_data[ptr+2])
        ptr += 3
        
        if q == 1:
            l -= 1
            r -= 1
            res_min = float('inf')
            res_max = float('-inf')
            
            l += n
            r += n
            while l <= r:
                if l % 2 == 1:
                    if tree_min[l] < res_min: res_min = tree_min[l]
                    if tree_max[l] > res_max: res_max = tree_max[l]
                    l += 1
                if r % 2 == 0:
                    if tree_min[r] < res_min: res_min = tree_min[r]
                    if tree_max[r] > res_max: res_max = tree_max[r]
                    r -= 1
                l //= 2
                r //= 2
            
            if res_min == res_max:
                results.append("draw")
            else:
                results.append("wins")
        else:
            idx = l - 1
            val = r
            idx += n
            tree_min[idx] = val
            tree_max[idx] = val
            while idx > 1:
                idx //= 2
                tree_min[idx] = min(tree_min[2 * idx], tree_min[2 * idx + 1])
                tree_max[idx] = max(tree_max[2 * idx], tree_max[2 * idx + 1])
                
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

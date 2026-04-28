import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    n = 100000
    
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = (pow(i, 2, 12345) + pow(i, 3, 23456))
        
    tree_min = [10**18] * (2 * (n + 1))
    tree_max = [-10**18] * (2 * (n + 1))
    
    for i in range(1, n + 1):
        tree_min[n + 1 + i] = a[i]
        tree_max[n + 1 + i] = a[i]
        
    for i in range(n, 0, -1):
        tree_min[i] = min(tree_min[2 * i], tree_min[2 * i + 1])
        tree_max[i] = max(tree_max[2 * i], tree_max[2 * i + 1])
        
    ptr = 1
    results = []
    
    size = n + 1
    for _ in range(k):
        x = int(input_data[ptr])
        y = int(input_data[ptr + 1])
        ptr += 2
        
        if x > 0:
            l, r = x + size, y + size
            res_min = 10**18
            res_max = -10**18
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
            results.append(str(res_max - res_min))
        else:
            idx = (-x) + size
            tree_min[idx] = y
            tree_max[idx] = y
            while idx > 1:
                idx //= 2
                m1 = min(tree_min[2 * idx], tree_min[2 * idx + 1])
                m2 = max(tree_max[2 * idx], tree_max[2 * idx + 1])
                if tree_min[idx] == m1 and tree_max[idx] == m2:
                    break
                tree_min[idx] = m1
                tree_max[idx] = m2
                
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

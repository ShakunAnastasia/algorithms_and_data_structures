import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    size = 1
    while size < n: size *= 2
    
    tree = [0] * (2 * size)
    for i in range(n):
        tree[size + i] = int(input_data[i + 1])
    
    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    
    m_idx = n + 1
    m = int(input_data[m_idx])
    ptr = m_idx + 1
    ans = []
    
    for _ in range(m):
        t = input_data[ptr]
        if t == '1':
            v = int(input_data[ptr + 1])
            ptr += 2
            if tree[1] <= v:
                ans.append(str(n))
            else:
                idx = 1
                while idx < size:
                    if tree[2 * idx] <= v:
                        v -= tree[2 * idx]
                        idx = 2 * idx + 1
                    else:
                        idx = 2 * idx
                ans.append(str(min(idx - size, n)))
        else:
            pos = int(input_data[ptr + 1]) - 1
            val = int(input_data[ptr + 2])
            ptr += 3
            pos += size
            tree[pos] = val
            while pos > 1:
                pos >>= 1
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                
    sys.stdout.write('\n'.join(ans) + '\n')

if __name__ == "__main__":
    solve()

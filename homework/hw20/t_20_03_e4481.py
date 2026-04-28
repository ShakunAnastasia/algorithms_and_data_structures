import sys
import math

sys.setrecursionlimit(200000)

def gcd(a, b):
    while b:
        a %= b
        a, b = b, a
    return a

class SegmentTree:
    def __init__(self, data, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self._build(data, 1, 0, n - 1)

    def _build(self, data, v, tl, tr):
        if tl == tr:
            self.tree[v] = data[tl]
        else:
            tm = (tl + tr) // 2
            self._build(data, 2 * v, tl, tm)
            self._build(data, 2 * v + 1, tm + 1, tr)
            self.tree[v] = math.gcd(self.tree[2 * v], self.tree[2 * v + 1])

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2 * v, tl, tm, pos, new_val)
            else:
                self.update(2 * v + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = math.gcd(self.tree[2 * v], self.tree[2 * v + 1])

    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return math.gcd(
            self.query(2 * v, tl, tm, l, min(r, tm)),
            self.query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
        )

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    n = int(input_data[idx])
    idx += 1
    
    a = []
    for _ in range(n):
        a.append(int(input_data[idx]))
        idx += 1
        
    m = int(input_data[idx])
    idx += 1
    
    st = SegmentTree(a, n)
    results = []
    
    for _ in range(m):
        q = int(input_data[idx])
        l = int(input_data[idx + 1])
        r = int(input_data[idx + 2])
        idx += 3
        
        if q == 1:
            results.append(str(st.query(1, 0, n - 1, l - 1, r - 1)))
        else:
            st.update(1, 0, n - 1, l - 1, r)
            
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

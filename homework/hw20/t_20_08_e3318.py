import sys

sys.setrecursionlimit(200000)

def solve():
    raw_data = sys.stdin.read().split()
    if not raw_data:
        return
    
    n = int(raw_data[0])
    a = [int(x) for x in raw_data[1:n+1]]
    m = int(raw_data[n+1])
    queries = raw_data[n+2:]

    NEXT_SQUARE = [(i * i) % 2010 for i in range(2010)]
    IS_FIXED = [False] * 2010
    for i in range(2010):
        if NEXT_SQUARE[i] == i:
            IS_FIXED[i] = True

    tree_sum = [0] * (4 * n)
    tree_fixed = [False] * (4 * n)

    def build(v, tl, tr):
        if tl == tr:
            val = a[tl]
            tree_sum[v] = val
            tree_fixed[v] = IS_FIXED[val]
            return
        tm = (tl + tr) >> 1
        v_l, v_r = v << 1, (v << 1) | 1
        build(v_l, tl, tm)
        build(v_r, tm + 1, tr)
        tree_sum[v] = tree_sum[v_l] + tree_sum[v_r]
        tree_fixed[v] = tree_fixed[v_l] and tree_fixed[v_r]

    def update(v, tl, tr, l, r):
        if tree_fixed[v]:
            return
        if tl == tr:
            v_new = NEXT_SQUARE[tree_sum[v]]
            tree_sum[v] = v_new
            tree_fixed[v] = IS_FIXED[v_new]
            return
        tm = (tl + tr) >> 1
        v_l, v_r = v << 1, (v << 1) | 1
        if l <= tm: update(v_l, tl, tm, l, r)
        if r > tm: update(v_r, tm + 1, tr, l, r)
        tree_sum[v] = tree_sum[v_l] + tree_sum[v_r]
        tree_fixed[v] = tree_fixed[v_l] and tree_fixed[v_r]

    def query(v, tl, tr, l, r):
        if l <= tl and tr <= r:
            return tree_sum[v]
        tm = (tl + tr) >> 1
        res = 0
        v_l = v << 1
        if l <= tm: res += query(v_l, tl, tm, l, r)
        if r > tm: res += query(v_l | 1, tm + 1, tr, l, r)
        return res

    build(1, 0, n - 1)
    output = []
    q_idx = 0
    for _ in range(m):
        t, l, r = queries[q_idx], int(queries[q_idx+1]) - 1, int(queries[q_idx+2]) - 1
        q_idx += 3
        if t == '1': 
            update(1, 0, n - 1, l, r)
        else: 
            output.append(str(query(1, 0, n - 1, l, r)))
    
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

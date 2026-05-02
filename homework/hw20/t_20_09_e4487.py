import sys

sys.setrecursionlimit(2000000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])
    
    t_mx = [0] * (4 * n)
    t_pre = [0] * (4 * n)
    t_suf = [0] * (4 * n)
    t_fv = [0] * (4 * n)
    t_lv = [0] * (4 * n)
    t_sz = [0] * (4 * n)

    def pull(v, vL, vR, szL, szR):
        t_fv[v] = t_fv[vL]
        t_lv[v] = t_lv[vR]
        t_sz[v] = szL + szR
        
        t_mx[v] = max(t_mx[vL], t_mx[vR])
        t_pre[v] = t_pre[vL]
        t_suf[v] = t_suf[vR]
        
        if t_lv[vL] <= t_fv[vR]:
            combined = t_suf[vL] + t_pre[vR]
            if combined > t_mx[v]:
                t_mx[v] = combined
            if t_pre[vL] == szL:
                t_pre[v] = szL + t_pre[vR]
            if t_suf[vR] == szR:
                t_suf[v] = szR + t_suf[vL]

    def build(v, tl, tr):
        if tl == tr:
            t_mx[v] = t_pre[v] = t_suf[v] = 1
            t_fv[v] = t_lv[v] = a[tl]
            t_sz[v] = 1
            return
        tm = (tl + tr) // 2
        vL, vR = 2 * v, 2 * v + 1
        build(vL, tl, tm)
        build(vR, tm + 1, tr)
        pull(v, vL, vR, tm - tl + 1, tr - tm)

    def update(v, tl, tr, pos, val):
        if tl == tr:
            t_fv[v] = t_lv[v] = val
            return
        tm = (tl + tr) // 2
        vL, vR = 2 * v, 2 * v + 1
        if pos <= tm:
            update(vL, tl, tm, pos, val)
        else:
            update(vR, tm + 1, tr, pos, val)
        pull(v, vL, vR, tm - tl + 1, tr - tm)

    def query(v, tl, tr, l, r):
        if l == tl and r == tr:
            return (t_mx[v], t_pre[v], t_suf[v], t_fv[v], t_lv[v], t_sz[v])
        
        tm = (tl + tr) // 2
        if r <= tm:
            return query(2 * v, tl, tm, l, r)
        elif l > tm:
            return query(2 * v + 1, tm + 1, tr, l, r)
        else:
            L = query(2 * v, tl, tm, l, tm)
            R = query(2 * v + 1, tm + 1, tr, tm + 1, r)
            
            res_mx = max(L[0], R[0])
            res_pre = L[1]
            res_suf = R[2]
            if L[4] <= R[3]:
                combined = L[2] + R[1]
                if combined > res_mx: res_mx = combined
                if L[1] == L[5]: res_pre = L[5] + R[1]
                if R[2] == R[5]: res_suf = R[5] + L[2]
            return (res_mx, res_pre, res_suf, L[3], R[4], L[5] + R[5])

    build(1, 0, n - 1)
    
    ptr = n + 2
    results = []
    for _ in range(m):
        type_q = int(input_data[ptr])
        l = int(input_data[ptr+1])
        r = int(input_data[ptr+2])
        ptr += 3
        
        if type_q == 1:
            results.append(str(query(1, 0, n - 1, l - 1, r - 1)[0]))
        else:
            update(1, 0, n - 1, l - 1, r)
            
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

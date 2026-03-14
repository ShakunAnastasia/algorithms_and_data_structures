import sys

sys.setrecursionlimit(300000)
try:
    sys.set_int_max_str_digits(400000)
except AttributeError:
    pass

def karatsuba(x, y):
    if not x: x = '0'
    if not y: y = '0'
    
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    
    n = max(len(x), len(y))
    m2 = n // 2
    
    x = x.zfill(n)
    y = y.zfill(n)
    
    h1, l1 = x[:-m2], x[-m2:]
    h2, l2 = y[:-m2], y[-m2:]
    
    z0 = karatsuba(l1, l2)
    z2 = karatsuba(h1, h2)
    z1 = karatsuba(str(int(l1) + int(h1)), str(int(l2) + int(h2)))
    
    return (z2 * (10 ** (2 * m2))) + ((z1 - z2 - z0) * (10 ** m2)) + z0

def solve():
    data = sys.stdin.read().split()
    if len(data) >= 2:
        print(karatsuba(data[0], data[1]))

if __name__ == "__main__":
    solve()

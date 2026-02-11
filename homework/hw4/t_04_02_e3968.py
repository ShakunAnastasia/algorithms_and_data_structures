import math

def f(x):
    return x**2 + math.sqrt(x)

def solve():
    try:
        line = input().strip()
        if not line:
            return
        c = float(line)
    except EOFError:
        return
    l = 0.0
    r = 100000.0

    for _ in range(100):
        m = (l + r) / 2.0
        
        if f(m) < c:
            l = m
        else:
            r = m
    print(f"{l:.6f}")

if __name__ == "__main__":
    solve()

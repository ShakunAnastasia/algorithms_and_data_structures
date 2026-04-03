import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    a = int(data[0])
    p = int(data[1])
    
    if a == 0:
        print(0)
        return
    
    stack = []
    while a > 0:
        stack.append(a % p)
        a //= p
        
    result = []
    while stack:
        digit = stack.pop()
        if digit > 9:
            result.append(f"[{digit}]")
        else:
            result.append(str(digit))
            
    print("".join(result))

if __name__ == "__main__":
    solve()

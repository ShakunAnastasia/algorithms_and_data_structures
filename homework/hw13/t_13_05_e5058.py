import sys

def solve():
    line = sys.stdin.read().strip()
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in line:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                print("no")
                return
                
    if not stack:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    solve()

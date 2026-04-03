import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    
    for char in reversed(s):
        if 'a' <= char <= 'z':
            stack.append((char, 3))
        else:
            op1_s, op1_p = stack.pop()
            op2_s, op2_p = stack.pop()
            
            curr_p = prec[char]
            
            if op1_p < curr_p:
                op1_s = "(" + op1_s + ")"
            
            if op2_p < curr_p or (op2_p == curr_p and char in ('-', '/')):
                op2_s = "(" + op2_s + ")"
            
            stack.append((op1_s + char + op2_s, curr_p))
    
    if stack:
        print(stack[0][0])

if __name__ == "__main__":
    solve()

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    
    used = [False] * (n + 1)
    current_permutation = []

    def backtrack():
        if len(current_permutation) == k:
            print(*(current_permutation))
            return
        
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                current_permutation.append(i)
                backtrack()
                current_permutation.pop()
                used[i] = False

    backtrack()

if __name__ == "__main__":
    solve()

import sys

sys.setrecursionlimit(100000)

def validate_bst_path(path, index, low, high):
    if index == len(path):
        return True
    
    current_val = path[index]
    
    if not (low < current_val < high):
        return False
    
    if index + 1 < len(path):
        next_val = path[index + 1]
        if next_val < current_val:
            return validate_bst_path(path, index + 1, low, current_val)
        else:
            return validate_bst_path(path, index + 1, current_val, high)
            
    return True

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    path = [int(x) for x in input_data]
    
    if validate_bst_path(path, 0, -float('inf'), float('inf')):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

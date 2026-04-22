import sys

def is_min_heap(arr, i, n):
    left = 2 * i
    right = 2 * i + 1
    
    if left <= n:
        if arr[i] > arr[left]:
            return False
        if not is_min_heap(arr, left, n):
            return False
            
    if right <= n:
        if arr[i] > arr[right]:
            return False
        if not is_min_heap(arr, right, n):
            return False
            
    return True

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    nums = [0] + [int(x) for x in input_data[1:]]
    
    if is_min_heap(nums, 1, n):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

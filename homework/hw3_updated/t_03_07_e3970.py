import sys

def find_lower_bound(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            high = mid
        else:
            low = mid + 1
    return low

def find_upper_bound(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid
        else:
            low = mid + 1
    return low

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    mutants = [int(x) for x in input_data[1:n + 1]]
    
    m = int(input_data[n + 1])
    queries = [int(x) for x in input_data[n + 2:n + 2 + m]]
    
    for color in queries:
        first_index = find_lower_bound(mutants, color)
        last_index = find_upper_bound(mutants, color)
        
        count = last_index - first_index
        print(count)

if __name__ == '__main__':
    main()

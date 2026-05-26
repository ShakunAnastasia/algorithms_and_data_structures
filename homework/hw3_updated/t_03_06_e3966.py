import sys

def check_butterfly(butterflies, target):
    low = 0
    high = len(butterflies) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if butterflies[mid] == target:
            return True
        elif butterflies[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    collection = [int(x) for x in input_data[1:n + 1]]
    
    m = int(input_data[n + 1])
    queries = [int(x) for x in input_data[n + 2:n + 2 + m]]
    
    for item in queries:
        if check_butterfly(collection, item):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

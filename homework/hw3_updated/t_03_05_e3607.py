import sys

def get_athletes_count(total, heights, min_bound, max_bound):
    total_found = 0
    for i in range(total):
        if min_bound <= heights[i] <= max_bound:
            total_found += 1
    return total_found

def main():
    while True:
        first_line = sys.stdin.readline()
        if not first_line:
            break
            
        n = int(first_line)
        athlete_heights = [int(val) for val in sys.stdin.readline().split()]
        
        limits = sys.stdin.readline().split()
        a = int(limits[0])
        b = int(limits[1])
        
        result = get_athletes_count(n, athlete_heights, a, b)
        print(result)

if __name__ == '__main__':
    main()

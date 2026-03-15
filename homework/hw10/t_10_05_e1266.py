import sys

def solve_tapes():
    lines = sys.stdin.read().splitlines()
    
    for line in lines:
        data = list(map(int, line.split()))
        if len(data) < 2:
            continue
            
        limit = data[0]
        count = data[1]
        items = data[2:2 + count]
        
        max_capacity = 0
        
        def find_max(idx, current):
            nonlocal max_capacity
            
            if current > limit:
                return
                
            if current > max_capacity:
                max_capacity = current
                
            if max_capacity == limit:
                return
                
            for i in range(idx, count):
                if current + items[i] <= limit:
                    find_max(i + 1, current + items[i])
                    
                    if max_capacity == limit:
                        return
                        
        find_max(0, 0)
        
        print(f"sum:{max_capacity}")

if __name__ == "__main__":
    solve_tapes()

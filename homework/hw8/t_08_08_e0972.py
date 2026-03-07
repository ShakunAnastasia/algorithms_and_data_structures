import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    times = []
    for i in range(n):
        h = int(input_data[1 + i*3])
        m = int(input_data[2 + i*3])
        s = int(input_data[3 + i*3])
        times.append([h, m, s])
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if times[j][0] < times[min_idx][0]:
                min_idx = j
            elif times[j][0] == times[min_idx][0]:
                if times[j][1] < times[min_idx][1]:
                    min_idx = j
                elif times[j][1] == times[min_idx][1]:
                    if times[j][2] < times[min_idx][2]:
                        min_idx = j
        
        times[i], times[min_idx] = times[min_idx], times[i]
        
    for t in times:
        print(t[0], t[1], t[2])

if __name__ == "__main__":
    solve()

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    words = input_data[1:]
    
    for i in range(1, len(words)):
        key = words[i]
        j = i - 1
        while j >= 0 and words[j] > key:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key
        
    for word in words:
        print(word)

if __name__ == "__main__":
    solve()

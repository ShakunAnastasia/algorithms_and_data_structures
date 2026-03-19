import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def solve():
    input_stream = sys.stdin.read().split()
    if not input_stream: 
        return
        
    p = 0
    while p < len(input_stream):
        n = int(input_stream[p])
        p += 1
        if n == 0: 
            break

        while True:
            if int(input_stream[p]) == 0:
                p += 1
                print()
                break

            target = []
            for _ in range(n):
                target.append(int(input_stream[p]))
                p += 1

            station = Stack()
            current_from_A = 1
            possible = True

            for car in target:
                while station.is_empty() or station.peek() != car:
                    if current_from_A <= n:
                        station.push(current_from_A)
                        current_from_A += 1
                    else:
                        possible = False
                        break
                if not possible: 
                    break
                station.pop()

            if possible:
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    solve()

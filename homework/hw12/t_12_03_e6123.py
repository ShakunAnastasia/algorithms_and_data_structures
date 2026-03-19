import sys

class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, n):
        self._items.append(n)
    
    def pop(self):
        return self._items.pop()
    
    def back(self):
        return self._items[-1]
    
    def size(self):
        return len(self._items)
    
    def clear(self):
        self._items = []

def run_simulation():
    s = Stack()
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        
        command = parts[0]
        
        if command == "push":
            s.push(parts[1])
            print("ok")
        elif command == "pop":
            if s.size() == 0:
                print("error")
            else:
                print(s.pop())
        elif command == "back":
            if s.size() == 0:
                print("error")
            else:
                print(s.back())
        elif command == "size":
            print(s.size())
        elif command == "clear":
            s.clear()
            print("ok")
        elif command == "exit":
            print("bye")
            break

if __name__ == "__main__":
    run_simulation()

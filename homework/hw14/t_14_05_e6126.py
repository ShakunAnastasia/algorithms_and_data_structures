import sys

class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, n):
        new_node = Node(n)
        if self._size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if self._size == 0:
            return "error"
        val = self.head.item
        self.head = self.head.next
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return val

    def front(self):
        if self._size == 0:
            return "error"
        return self.head.item

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return "ok"

def main():
    q = Queue()
    input_data = sys.stdin.read().splitlines()
    
    for line in input_data:
        parts = line.split()
        if not parts:
            continue
            
        command = parts[0]
        
        if command == "push":
            print(q.push(parts[1]))
        elif command == "pop":
            print(q.pop())
        elif command == "front":
            print(q.front())
        elif command == "size":
            print(q.size())
        elif command == "clear":
            print(q.clear())
        elif command == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()

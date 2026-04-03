import sys

class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, n):
        new_node = Node(n)
        if self._size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1
        return "ok"

    def push_back(self, n):
        new_node = Node(n)
        if self._size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self._size == 0:
            return "error"
        val = self.head.item
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return val

    def pop_back(self):
        if self._size == 0:
            return "error"
        val = self.tail.item
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    def front(self):
        if self._size == 0:
            return "error"
        return self.head.item

    def back(self):
        if self._size == 0:
            return "error"
        return self.tail.item

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return "ok"

def main():
    dq = Deque()
    input_data = sys.stdin.read().splitlines()
    
    for line in input_data:
        parts = line.split()
        if not parts:
            continue
            
        command = parts[0]
        
        if command == "push_front":
            print(dq.push_front(parts[1]))
        elif command == "push_back":
            print(dq.push_back(parts[1]))
        elif command == "pop_front":
            print(dq.pop_front())
        elif command == "pop_back":
            print(dq.pop_back())
        elif command == "front":
            print(dq.front())
        elif command == "back":
            print(dq.back())
        elif command == "size":
            print(dq.size())
        elif command == "clear":
            print(dq.clear())
        elif command == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()

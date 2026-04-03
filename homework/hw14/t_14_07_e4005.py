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

    def pop(self):
        if self._size == 0:
            return None
        val = self.head.item
        self.head = self.head.next
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return val

    def size(self):
        return self._size

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    half = n // 2
    
    q1 = Queue()
    q2 = Queue()
    
    for i in range(half):
        q1.push(int(input_data[1 + i]))
    for i in range(half):
        q2.push(int(input_data[1 + half + i]))
        
    moves = 0
    limit = 200000
    
    while q1.size() > 0 and q2.size() > 0 and moves < limit:
        moves += 1
        c1 = q1.pop()
        c2 = q2.pop()
        
        if c1 == 0 and c2 == n - 1:
            first_wins = True
        elif c2 == 0 and c1 == n - 1:
            first_wins = False
        else:
            first_wins = c1 > c2
            
        if first_wins:
            q1.push(c1)
            q1.push(c2)
        else:
            q2.push(c1)
            q2.push(c2)
            
    if q1.size() == 0:
        sys.stdout.write(f"second {moves}\n")
    elif q2.size() == 0:
        sys.stdout.write(f"first {moves}\n")
    else:
        sys.stdout.write("draw\n")

if __name__ == "__main__":
    solve()

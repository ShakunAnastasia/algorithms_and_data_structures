import sys

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def RotateRight(self, k: int) -> None:
        if not self.head or not self.head.next:
            return
        
        n = 1
        curr = self.head
        while curr.next:
            curr = curr.next
            n += 1
        
        k = k % n
        if k == 0:
            return
            
        curr.next = self.head
        
        steps_to_new_tail = n - k
        new_tail = self.head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        self.head = new_tail.next
        self.tail = new_tail
        new_tail.next = None

    def Print(self) -> None:
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        print(" ".join(res))

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    values = input_data[1:n+1]
    queries = input_data[n+1:]
    
    linked_list = List()
    for v in values:
        linked_list.AddToTail(int(v))
    
    for k_str in queries:
        k = int(k_str)
        linked_list.RotateRight(k)
        linked_list.Print()

if __name__ == "__main__":
    main()

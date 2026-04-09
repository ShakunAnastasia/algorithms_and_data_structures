import sys

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None

class List:
    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def ReorderList(self) -> None:
        if not self.head or not self.head.next:
            return

        slow, fast = self.head, self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev

        first = self.head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        curr = self.head
        while curr.next:
            curr = curr.next
        self.tail = curr

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
    nums = input_data[1:n+1]
    
    my_list = List()
    for x in nums:
        my_list.addToTail(int(x))
    
    my_list.ReorderList()
    my_list.Print()

if __name__ == "__main__":
    main()

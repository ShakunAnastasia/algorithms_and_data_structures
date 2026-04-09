import sys

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        print(" ".join(res))

    def _recursive_reverse(self, node, res):
        if node is None:
            return
        self._recursive_reverse(node.next, res)
        res.append(str(node.data))

    def PrintReverse(self) -> None:
        res = []
        self._recursive_reverse(self.head, res)
        print(" ".join(res))

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    vals = input_data[1:n+1]
    
    linked_list = List()
    for v in vals:
        linked_list.addToTail(int(v))
    
    linked_list.Print()
    linked_list.PrintReverse()

if __name__ == "__main__":
    main()

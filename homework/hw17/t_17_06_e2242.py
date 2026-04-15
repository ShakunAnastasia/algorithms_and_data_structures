import sys

sys.setrecursionlimit(100000)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def get_preorder(node, result):
    if node:
        result.append(node.key)
        get_preorder(node.left, result)
        get_preorder(node.right, result)

def main():
    lines = []
    for line in sys.stdin:
        l = line.strip()
        if not l:
            continue
        if l == '*':
            break
        lines.append(l)
    
    if not lines:
        return

    root = None
    for i in range(len(lines) - 1, -1, -1):
        for char in lines[i]:
            root = insert(root, char)
    
    result = []
    get_preorder(root, result)
    print("".join(result))

if __name__ == "__main__":
    main()

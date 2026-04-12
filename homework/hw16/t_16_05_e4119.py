import sys

class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.children = {}

def insert_path_recursive(node, parts):
    if not parts:
        return
    
    dir_name = parts[0]
    if dir_name not in node.children:
        node.children[dir_name] = DirectoryNode(dir_name)
    
    insert_path_recursive(node.children[dir_name], parts[1:])

def print_tree_recursive(node, depth):
    names = sorted(node.children.keys())
    for name in names:
        print(" " * depth + name)
        print_tree_recursive(node.children[name], depth + 1)

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    try:
        n = int(input_data[0])
    except (ValueError, IndexError):
        return
        
    root = DirectoryNode("root")
    
    for i in range(1, n + 1):
        if i < len(input_data):
            path = input_data[i]
            insert_path_recursive(root, path.split('\\'))
    
    print_tree_recursive(root, 0)

if __name__ == "__main__":
    solve()

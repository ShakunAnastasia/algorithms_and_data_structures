import sys

sys.setrecursionlimit(2000)

class GameNode:
    def __init__(self, node_id):
        self.id = node_id
        self.children = []
        self.value = None
        self.is_leaf = False

def evaluate_minimax(node, is_maximizing):
    if node.is_leaf:
        return node.value
    
    if is_maximizing:
        best_val = -float('inf')
        for child in node.children:
            best_val = max(best_val, evaluate_minimax(child, False))
        return best_val
    else:
        best_val = float('inf')
        for child in node.children:
            best_val = min(best_val, evaluate_minimax(child, True))
        return best_val

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    nodes = [GameNode(i) for i in range(n + 1)]
    
    for i in range(2, n + 1):
        parts = input_data[i-1].split()
        node_type = parts[0]
        parent_id = int(parts[1])
        
        if node_type == 'L':
            nodes[i].is_leaf = True
            nodes[i].value = int(parts[2])
        
        nodes[parent_id].children.append(nodes[i])
    
    result = evaluate_minimax(nodes[1], True)
    
    if result > 0:
        print("+1")
    elif result < 0:
        print("-1")
    else:
        print("0")

if __name__ == "__main__":
    solve()

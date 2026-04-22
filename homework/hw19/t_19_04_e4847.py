import sys

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.pos_map = {}

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos_map[self.heap[i][1]] = i
        self.pos_map[self.heap[j][1]] = j

    def _sift_up(self, idx):
        if idx == 0:
            return
        parent = (idx - 1) // 2
        if self.heap[idx][0] > self.heap[parent][0]:
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        n = len(self.heap)

        if left < n and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < n and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != idx:
            self._swap(idx, largest)
            self._sift_down(largest)

    def add(self, node_id, priority):
        self.heap.append([priority, node_id])
        idx = len(self.heap) - 1
        self.pos_map[node_id] = idx
        self._sift_up(idx)

    def pop(self):
        if not self.heap:
            return None
        
        top_priority, top_id = self.heap[0]
        last_node = self.heap.pop()
        del self.pos_map[top_id]

        if self.heap:
            self.heap[0] = last_node
            self.pos_map[last_node[1]] = 0
            self._sift_down(0)
            
        return top_id, top_priority

    def change(self, node_id, new_priority):
        idx = self.pos_map[node_id]
        old_priority = self.heap[idx][0]
        self.heap[idx][0] = new_priority
        
        if new_priority > old_priority:
            self._sift_up(idx)
        else:
            self._sift_down(idx)

def solve():
    pq = PriorityQueue()
    input_data = sys.stdin.read().splitlines()
    
    for line in input_data:
        parts = line.split()
        if not parts:
            continue
            
        command = parts[0]
        
        if command == "ADD":
            pq.add(parts[1], int(parts[2]))
        elif command == "POP":
            res = pq.pop()
            if res:
                print(f"{res[0]} {res[1]}")
        elif command == "CHANGE":
            pq.change(parts[1], int(parts[2]))

if __name__ == "__main__":
    solve()

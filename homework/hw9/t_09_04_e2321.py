import sys

sys.setrecursionlimit(2000)

def quick_sort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quick_sort(a, low, p)
        quick_sort(a, p + 1, high)

def partition(a, low, high):
    pivot = a[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while a[i] < pivot:
            i += 1
        j -= 1
        while a[j] > pivot:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:]]
    if n > 0:
        quick_sort(arr, 0, n - 1)
    print(*(arr))

if __name__ == "__main__":
    solve()

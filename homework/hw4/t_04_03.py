low, high = 0.0, 10.0
for _ in range(100):
    mid = (low + high) / 2
    if mid**3 + mid + 1 < 5:
        low = mid
    else:
        high = mid
print(f"Відповідь 4.3: {low:.2f}")

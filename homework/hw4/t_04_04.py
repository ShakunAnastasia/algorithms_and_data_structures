import math
low, high = 1.6, 3.0
for _ in range(100):
    mid = (low + high) / 2
    if math.sin(mid) > mid / 3:
        low = mid
    else:
        high = mid
print(f"Відповідь 4.4: {low:.2f}")

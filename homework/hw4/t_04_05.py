low, high = 0.0, 2.0
for _ in range(100):
    mid = (low + high) / 2
    if mid**3 + 4*mid**2 + mid - 6 < 0:
        low = mid
    else:
        high = mid
print(f"Відповідь 4.5: {low:.2f}")

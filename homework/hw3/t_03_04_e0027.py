n = int(input())

s = bin(n)[2:]

max_m = n

for _ in range(len(s)):
    s = s[1:] + s[0]
    
    current_val = int(s, 2)
    if current_val > max_m:
        max_m = current_val

print(max_m)

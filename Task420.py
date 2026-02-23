m = int(input().strip())

g = 0
n = 0

for _ in range(m):
    parts = input().strip().split()
    if not parts:
        continue
    scope = parts[0]
    val = int(parts[1])
    
    if scope == "global":
        g += val
    elif scope == "nonlocal":
        n += val

print(f"{g} {n}")


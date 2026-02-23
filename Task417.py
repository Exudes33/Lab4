import math

R = float(input().strip())
x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

dx = x2 - x1
dy = y2 - y1

a = dx**2 + dy**2
b = 2 * (x1 * dx + y1 * dy)
c = x1**2 + y1**2 - R**2

if a == 0:
    print("0.0000000000")
else:
    D = b**2 - 4 * a * c
    if D < 0:
        print("0.0000000000")
    else:
        t1 = (-b - math.sqrt(D)) / (2 * a)
        t2 = (-b + math.sqrt(D)) / (2 * a)
        
        t_start = max(0.0, min(t1, t2))
        t_end = min(1.0, max(t1, t2))
        
        if t_start <= t_end:
            ans = (t_end - t_start) * math.hypot(dx, dy)
            print(f"{ans:.10f}")
        else:
            print("0.0000000000")
          

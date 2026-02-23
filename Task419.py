import math

R = float(input().strip())
x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

d1 = math.hypot(x1, y1)
d2 = math.hypot(x2, y2)

val = (x1 * x2 + y1 * y2) / (d1 * d2)
val = max(-1.0, min(1.0, val))
delta_theta = math.acos(val)

alpha1 = math.acos(R / d1)
alpha2 = math.acos(R / d2)

if delta_theta > alpha1 + alpha2:
    L1 = math.sqrt(d1**2 - R**2)
    L2 = math.sqrt(d2**2 - R**2)
    arc = R * (delta_theta - alpha1 - alpha2)
    ans = L1 + L2 + arc
else:
    ans = math.hypot(x1 - x2, y1 - y2)

print(f"{ans:.10f}")

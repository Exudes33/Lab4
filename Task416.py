from datetime import datetime

s1 = input().strip().replace(" UTC", " ")
s2 = input().strip().replace(" UTC", " ")

d1 = datetime.strptime(s1, "%Y-%m-%d %H:%M:%S %z")
d2 = datetime.strptime(s2, "%Y-%m-%d %H:%M:%S %z")

print(int((d2 - d1).total_seconds()))


import json

def find_diff(a, b, path=""):
    diffs = {}
    if isinstance(a, dict) and isinstance(b, dict):
        for key in set(a.keys()) | set(b.keys()):
            new_path = f"{path}.{key}" if path else key
            if key not in a:
                diffs[new_path] = ("<missing>", b[key])
            elif key not in b:
                diffs[new_path] = (a[key], "<missing>")
            else:
                diffs.update(find_diff(a[key], b[key], new_path))
    elif a != b:
        diffs[path] = (a, b)
    return diffs

def fmt(val):
    return val if val == "<missing>" else json.dumps(val, separators=(',', ':'))

A = json.loads(input())
B = json.loads(input())
diffs = find_diff(A, B)

if not diffs:
    print("No differences")
else:
    for path in sorted(diffs.keys()):
        v1, v2 = diffs[path]
        print(f"{path} : {fmt(v1)} -> {fmt(v2)}")
      

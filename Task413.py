import json

data = json.loads(input())
q = int(input())

for _ in range(q):
    query = input().strip()
    parts = [p for p in query.replace('[', '.').replace(']', '').split('.') if p]
    
    current = data
    found = True
    
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list) and part.isdigit():
            idx = int(part)
            if 0 <= idx < len(current):
                current = current[idx]
            else:
                found = False
                break
        else:
            found = False
            break
            
    if found:
        print(json.dumps(current, separators=(',', ':')))
    else:
        print("NOT_FOUND")
      

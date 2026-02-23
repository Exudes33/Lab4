import json

def apply_patch(source, patch):
    for key, value in patch.items():
        if value is None:
            if key in source:
                del source[key]
        elif isinstance(value, dict) and isinstance(source.get(key), dict):
            apply_patch(source[key], value)
        else:
            source[key] = value

source_data = json.loads(input())
patch_data = json.loads(input())

apply_patch(source_data, patch_data)
print(json.dumps(source_data, separators=(',', ':'), sort_keys=True))


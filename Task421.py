import importlib

q = int(input().strip())

for _ in range(q):
    mod_path, attr = input().strip().split()
    try:
        mod = importlib.import_module(mod_path)
        if not hasattr(mod, attr):
            print("ATTRIBUTE_NOT_FOUND")
        else:
            obj = getattr(mod, attr)
            if callable(obj):
                print("CALLABLE")
            else:
                print("VALUE")
    except Exception:
        print("MODULE_NOT_FOUND")
      

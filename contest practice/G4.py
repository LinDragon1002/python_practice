def braves(a):
    correct = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    missing = correct - set(a)
    return sorted(missing)
    


a = input()
print(braves(a))
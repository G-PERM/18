words = ["cat", "python", "code", "ai", "logic"]
a = {x : len(x) for x in words if len(x) > 3}
print(a)
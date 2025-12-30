n = [3, 7, 12, 45, 8, 123, 9]
result = {x: len(str(x)) for x in n if x > 10}
print(result)
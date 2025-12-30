n = [1, 2, 2, 3, 3, 3, 4, 5, 5]
a = {x : n.count(x) for x in n if n.count(x) > 1}
print(a)
n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [x for sub in n for x in sub if x % 2 == 0 or x % 3 == 0]
print(a)
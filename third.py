n = [[1, 2, 3], [4, 5, 6], [7, 8]]
a = [y for sub in n for y in sub if y % 2 == 0]
print(a)
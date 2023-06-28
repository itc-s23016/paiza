def f(matrix):
    return "OK" if t >= 3 else "NG"


matrix = [(d, e) for [d, e] in [input().split() for _ in range(5)]]
a = list(d == e for d, e in matrix)
t = a.count(True)
result = f(matrix)
print(result)

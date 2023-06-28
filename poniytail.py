matrix = [(d, e) for [d, e] in [input().split() for _ in range(5)]]
a = list(d == e for d, e in matrix)
t = a.count(True)
if t >= 3:
    print("OK")
else:
    print("NG")

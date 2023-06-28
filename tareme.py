def f(s, n):
    return "OK" if s >= n else "NG"


[s, n] = [int(_) for _ in input().split()]
result = f(s, n)
print(result)

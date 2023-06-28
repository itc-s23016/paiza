def f(s, t):
    return (t - 1) * b + a + (s - t) * b


[s, t] = [int(input()) for _ in range(2)]
a = "+"
b = "-"
result = f(s, t)
print(result)

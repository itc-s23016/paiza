def f(n, m, s, t):
    return len(t)


n, m = map(int, input().split())
s, t = [input() for _ in range(2)]
for a in s:
    if a in t:
        t = t.replace(a, "", 1)
result = f(n, m, s, t)
print(result)

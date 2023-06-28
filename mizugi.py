n, m = map(int, input().split())
s, t = [input() for _ in range(2)]
for a in s:
    if a in t:
        t = t.replace(a, "", 1)
print(len(t))

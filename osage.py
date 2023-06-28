[n, m] = [int(input()) for _ in range(2)]
ts = [int(input()) for _ in range(m)]
t = n * 60
c = 0
for i in ts:
    if i < t:
        t -= i
        c += 1
    else:
        break
if c == m:
    print("OK")
else:
    print(c)

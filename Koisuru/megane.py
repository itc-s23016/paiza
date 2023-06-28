N = int(input())
alist = map(int, input().split()[:N])
b = [a for a in alist]
b.sort()
c = (N + 1) // 2
print(b[c - 1])

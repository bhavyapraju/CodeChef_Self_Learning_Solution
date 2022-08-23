n, m, k = map(int, input().split())
s = 0

for _ in range(n):
    a = list(map(int, input().split()))
    b = sum(a)-a[-1]
    if b >= m and a[-1] <= 10:
        s += 1
print(s)
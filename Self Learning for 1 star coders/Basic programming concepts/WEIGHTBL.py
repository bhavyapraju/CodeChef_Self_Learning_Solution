for _ in range(int(input())):
    w1, w2, x1, x2, m = map(int, input().split())
    d = w2 - w1
    if m*x1 <= d <= m*x2:
        print(1)
    else:
        print(0)
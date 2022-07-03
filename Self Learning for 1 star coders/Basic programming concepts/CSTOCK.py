for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a = a + (a*d) / 100
    if a >= b and a <= c:
        print("YES")
    else:
        print('NO')
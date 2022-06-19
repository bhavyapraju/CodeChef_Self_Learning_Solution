for _ in range(int(input())):
    n, a, b, c = map(int, input().split())

    if a+c <= b:
        if a+c >= n:
            print("YES")
        else:
            print("NO")
    else:
        if n <= b:
            print('YES')
        else:
            print("NO")
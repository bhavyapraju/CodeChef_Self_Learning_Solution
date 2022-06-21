for _ in range(int(input())):
    a, b, x = map(int, input().split(' '))
    num = (b - a) // x
    print(num)
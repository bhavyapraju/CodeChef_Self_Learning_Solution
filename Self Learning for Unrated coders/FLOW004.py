n = int(input())
for i in range(n):
    num = str(input())
    a, b = num[0], num[-1]
    print(int(a) + int(b))

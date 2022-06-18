for _ in range(int(input())):
    num = int(input())
    count = 0
    for j in str(num):
        if j == '4':
            count += 1
    print(count)
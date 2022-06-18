for _ in range(int(input())):
    l = list(map(int, input().split(' ')))
    print(abs(abs(l[1]-l[0])-l[0]))
for _ in range(int(input())):
    li = [int(x) for x in input().split()]
    a, b, c = li[0], li[1], li[2]
    print(max(a, b, c) + sum(li) - max(a, b, c) - min(a, b, c))
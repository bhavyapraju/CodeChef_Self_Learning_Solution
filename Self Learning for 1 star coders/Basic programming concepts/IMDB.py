for _ in range(int(input())):
    rating = 0
    a, b = map(int, input().split())
    for i in range(a):
        s, r = map(int, input().split())
        if s > b:
            continue
        if r > rating:
            rating = r
    print(rating)
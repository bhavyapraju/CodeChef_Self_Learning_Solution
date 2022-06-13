T = int(input())
for i in range(T):
    n, p, x, y = map(int, str(input()).split(' '))
    arr = [int(i) for i in str(input()).split(' ')]

    count = 0
    for idx in range(p):
        count += x if arr[idx] == 0 else y
    
    print(count)
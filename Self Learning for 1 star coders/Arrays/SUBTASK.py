t = int(input())
for i in range(t):
    N,M,K = map(int,input().split())
    x = list(map(int,input().split()))
    if sum(x) == N:
        print(100)
    y = []
    for i in range(M):
        y.append(x[i])
    if sum(y) == M :
        print(K)
    else : 
        print(0)
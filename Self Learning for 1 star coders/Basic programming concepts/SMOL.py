T = int(input())
for i in range(T):
    N,K = map(int, input().split())
    if(K == 0):
        print(N)
    elif(N < K):
        print(N)
    elif(N >= K):
        print(N % K)
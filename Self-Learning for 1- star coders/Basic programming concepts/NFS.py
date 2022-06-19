import math
T = int(input())
for x in range(T):
    U,V,A,S = map(int, input().split())
    if(U <= V):
        print("YES")
    elif(U**2 - 2*A*S >= 0):
        V1 = math.sqrt(U**2 - 2*A*S)
        if(V1<=V):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
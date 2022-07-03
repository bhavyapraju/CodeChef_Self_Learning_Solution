for _ in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    e=abs(a-c)+abs(b-d)
    if(k>=e and k%2==e%2):
        print("YES")
    else:
        print("NO")
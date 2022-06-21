T=int(input())

for i in range(T):
    A,B,A1,B1,A2,B2 = map(int, input().split())
    if A==A1 and B==B1:
        print("1")
    elif A==B1 and B==A1:
        print("1")
    elif A==A2 and B==B2:
        print("2")
    elif A==B2 and B==A2:
        print("2")
    else:
        print("0")

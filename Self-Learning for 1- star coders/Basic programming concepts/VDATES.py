for i in range(int(input())):
    d,l,r = map(int, input().split())
    if(l<=d<=r):
        print("Take second dose now")
    if(d<l):
        print("Too Early")
    if(d>r):
        print("Too Late")
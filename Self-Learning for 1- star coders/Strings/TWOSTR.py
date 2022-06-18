# cook your dish here
n=int(input())
for i in range(n):
    a=input()
    b=input()
    c=len(a)
    for i in range(c):
        if a[i]!="?" and b[i]!="?":
            if a[i]!=b[i]:
                print("No")
                break
    else:
        print("Yes")
                
            
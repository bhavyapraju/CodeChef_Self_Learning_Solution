t = int(input())
while t > 0:
    n = int(input())
    el = [1,2,3,4,5,6,7]
    balloons = list(map(int,input().split()))
    ct = 0
    it = 0
    while (len(el)!=0):
        if balloons[it] in el:
            ct+=1
            el.remove(balloons[it])
            it+=1
        else:
            ct+=1 
            it+=1
    print(ct)
    t-=1
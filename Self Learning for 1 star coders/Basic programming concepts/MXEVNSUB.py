from math import ceil

def mapInput():
    return map(int, input().split())
def intInput():
    return int(input())
def listInput():
    return list(mapInput())


for _ in range(intInput()):
    n = intInput()
    
    m = ceil(n/2)
    print((n if m%2==0 else n-1))
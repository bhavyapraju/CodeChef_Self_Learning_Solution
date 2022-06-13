n = int(input())
for i in range(n):
    s = str(input())
    temp = [int(i) for i in s]
    print(sum(temp))
for _ in range(int(input())):
    S = str(input())
    if S[0] == '0':
        count = 0
    else:
        count = 1
    for s in range(1, len(S)):
        if S[s] != S[s - 1]:
            count += 1
    print(count)
x = int(input())
for i in range(x):
    s = input()
    if s=='B' or s=='b':
        print("BattleShip")
    elif s=='c' or s=='C':
        print("Cruiser")
    elif s=='d' or s=='D':
        print("Destroyer")
    else:
        print("Frigate")
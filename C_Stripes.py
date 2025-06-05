for _ in range(int(input())):
    l = []
    for i in range(8):
        l.append(input())

    row = col = float("inf")
    for i in range(8):
        if l[i][0] == "R":
            row = i
            break
    if l[row][7] == "R":
        print("R")
    else:
        print("B")
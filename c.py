while True:
    x, y = map(int, input().split())

    if x == -1 and y == -1:
        break

    posiableL = [i for i in range(100)]

    up = len(posiableL[x:y])
    down = 100-len(posiableL[y:x:-1])
    if up < down or down == 0:
        print(up)
    else:
        print(down)

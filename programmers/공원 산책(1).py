def solution(park, routes):
    x = 0
    y = 0
    for test1 in range(len(park)):
        for test2 in range(len(park[test1])):
            if park[test1][test2] == "S":
                x = test2
                y = test1
                break
    for i in routes:
        xx = x
        yy = y
        for j in range(int(i[2])):            
            if i[0] == "N" and yy != 0 and park[yy-1][xx] != "X":
                yy -= 1
                if j == int(i[2])-1:
                    y = yy
            elif i[0] == "S" and yy != len(park[0])-1 and park[yy+1][xx] != "X":
                yy += 1
                if j == int(i[2])-1:
                    y = yy
            elif i[0] == "W" and xx != 0 and park[yy][xx-1] != "X":
                xx -= 1
                if j == int(i[2])-1:
                    x = xx
            elif i[0] == "E" and xx != len(park[0])-1 and park[yy][xx+1] != "X":
                xx += 1
                if j == int(i[2])-1:
                    x = xx
    return [y,x]
def solution(wallpaper):
    box_x = []
    box_y = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                box_x.append(i)
                box_y.append(j)
    box_x.sort()
    box_y.sort()
    return box_x[0],box_y[0],box_x[-1]+1,box_y[-1]+1
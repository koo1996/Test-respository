def solution(food):
    temp1 = ''
    temp2 = ''
    for i in range(1,len(food)):
        cnt = 0
        if food[i] % 2 == 1:
            cnt = (food[i] - 1) / 2
        else:
            cnt = food[i] / 2
        temp1 += str(i) * int(cnt)
        temp2 += str(i) * int(cnt)

    return temp1+"0"+temp2[::-1]
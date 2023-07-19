def solution(X, Y):
    box_X = [0 for _ in range(10)]
    box_Y = [0 for _ in range(10)]
    answer = ''
    for i in X:
        box_X[int(i)] += 1

    for j in Y:
        box_Y[int(j)] += 1

    for k in range(len(box_X)):
        answer += str(k) * min(box_X[k],box_Y[k])

    answer = answer[::-1]

    if len(answer) == 0:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return answer
def solution(k, score):
    result_ = []
    answer = []
    for i in score:
        answer.append(i)
        if len(answer) <= k:
            result_.append(min(answer))
        else:
            answer.sort()
            answer.pop(0)
            result_.append(min(answer))
    return result_

    #꿀팁 remove 이용 
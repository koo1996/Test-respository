def solution(weights):
    answer = 0
    dic = {}

    for i in weights:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for j in dic:
        if dic[j] > 1:
            answer += dic[j] * (dic[j] - 1) / 2
        if j*2 in dic:
            answer += dic[j] * dic[j*2]
        if j*(3/2) in dic:
            answer += dic[j] * dic[j*(3/2)]
        if j*(4/3) in dic:
            answer += dic[j] * dic[j*(4/3)]
    return answer
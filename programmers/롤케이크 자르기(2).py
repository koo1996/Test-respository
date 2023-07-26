def solution(topping):
    answer = 0
    dic1 = {} #나
    dic2 = {} #동생
    for i in topping: #topping 전부를 dic1에 추가
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1

    for i in topping: #동생(dic2)에게 하나씩 주면 나(dic1)는 하나씩 뺀다.
        if i in dic2:          
            dic2[i] += 1          
        else:
            dic2[i] = 1
        dic1[i] -= 1

        if dic1[i] == 0: #value가 0이 되는 토핑들은 삭제한다.
            del dic1[i]

        if len(dic1) == len(dic2): #나, 동생 길이가 같아지면 answer 1씩 더한다.
            answer += 1

    return answer
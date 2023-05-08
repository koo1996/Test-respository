def solution(x, n):   
    answer = []
    result = 0
    for i in range(n):
        result += x
        answer.append(result)
    return answer
def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        if k < int(intStrs[i][s:s+l]):
            answer.append(int(intStrs[i][s:s+l]))            
    return answer
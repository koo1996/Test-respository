def solution(arr, queries):

    answer2 = []
    for s,e,k in queries:
        answer1 = []
        for i in range(s,e+1):
            if arr[i] > k:
                answer1.append(arr[i])
        if len(answer1) > 0:
            answer2.append(min(answer1))            
        else:
            answer2.append(-1)
    return answer2

##
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer
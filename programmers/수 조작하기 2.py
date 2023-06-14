def solution(numLog):
    answer = ""
    for test in range(1,len(numLog)):
        if numLog[test] - numLog[test-1] == 1:
            answer += "w"
        elif numLog[test] - numLog[test-1] == -1:
            answer += "s"
        elif numLog[test] - numLog[test-1] == 10:
            answer += "d"
        else:
            answer += "a"
    return answer
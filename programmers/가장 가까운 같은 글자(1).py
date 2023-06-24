def solution(s):
    answer = []
    s_dic = {}
    for i in range(len(s)):
        if s[i] in s_dic:
            answer.append(i - s_dic[s[i]])
        else:
            answer.append(-1)
        s_dic[s[i]] = i
    return answer
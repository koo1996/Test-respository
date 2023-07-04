def solution(participant, completion):
    d = {}
    for i in participant:
        d[i] = d.get(i,0) + 1

    for j in completion:
        d[j] -= 1 

    for key,value in d.items():
        if value > 0:
            return key
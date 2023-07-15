def solution(dartResult):
    answer = ''
    score = []
    for i in dartResult:        
        if i.isdigit():
            answer += i
        elif i == "S":
            score.append(int(answer) ** 1)
            answer = ''
        elif i == "D":
            score.append(int(answer) ** 2)
            answer = ''
        elif i == "T":
            score.append(int(answer) ** 3)
            answer = ''
        elif i == "#":
            score[-1] = score[-1] * -1
        elif i == "*":
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[0] = score[0] * 2
    return sum(score)
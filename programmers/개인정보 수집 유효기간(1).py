def date_time(t):
    year, month, day = map(int,t.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    for i in terms:
        i = i.split()
        print(i)
        for j in range(len(privacies)):
            if i[0] in privacies[j]:
                privacies[j] = privacies[j].replace(i[0],'')
                if date_time(today) - (date_time(privacies[j]) + int(i[1]) * 28 - 1) > 0:
                    answer.append(j+1)        
    answer.sort()
    return answer
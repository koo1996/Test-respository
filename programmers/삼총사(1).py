def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)):
            for k in range(j+1,len(number)):
                if not number[i] + number[j] + number[k]:
                    answer += 1
    return answer
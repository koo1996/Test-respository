def solution(x):
    result = 0
    answer = True
    x = str(x)
    for i in range(len(x)):
        result += int(x[i])
    if int(x) % result != 0:
        answer = False    
    return answer

# 풀이
def solution(n):
    return n%sum(int(x) for x in str(n)) == 0
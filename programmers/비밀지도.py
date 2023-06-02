def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        test = bin(arr1[i] | arr2[i])
        test = test[2:].zfill(n)
        test = test.replace("1", "#").replace("0", " ")
        answer.append(test)        
    return answer
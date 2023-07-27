def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        list_ = []        
        for k in range(len(arr2[0])):
            sum = 0
            for j in range(len(arr2)):            
                sum += arr1[i][j] * arr2[j][k]
            list_.append(sum)
        answer.append(list_)
    return answer
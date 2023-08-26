def solution(arr, intervals):    
    return [arr[j] for i in intervals for j in range(i[0],i[1]+1)]
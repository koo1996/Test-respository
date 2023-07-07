def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum_ = nums[i] + nums[j] + nums[k]
                for l in range(2, sum_):
                    if sum_ % l == 0:
                        break                    
                else:
                    answer += 1

    return answer
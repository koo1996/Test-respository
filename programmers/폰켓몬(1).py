def solution(nums):
    nums1 = list(set(nums))
    return len(nums) // 2 if len(nums1) >= (len(nums) // 2) else len(nums1)